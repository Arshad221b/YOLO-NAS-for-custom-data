from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
import torch 
import torch.nn as nn 
from super_gradients.training import models
from config.model_config import CONFIG

app = Flask(__name__)
app.config['UPLOAD_FOLDER']         = CONFIG['upload_folder']
app.config['OUTPUT_FOLDER']         = CONFIG['output_folder']
app.config['ALLOWED_EXTENSIONS']    = CONFIG['allowed_extensions']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part in the request!'

    device        = 0 if torch.cuda.is_available() else "cpu"
    file          = request.files['file']
    model_path    = CONFIG['model_path']
    model         = models.get('yolo_nas_l',
                            num_classes=4,
                            checkpoint_path=model_path)
    
    if file and allowed_file(file.filename):
        filename    = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        file        = model.to(device).predict(os.path.join(app.config['UPLOAD_FOLDER'], filename))#.save(output_path)
        filepath    = os.path.join(app.config['OUTPUT_FOLDER'], filename)
        file.save(filepath)

        output_path = os.path.join('/Users/arshad_221b/Downloads/Projects/YOLO/traffic/source/output/', '{}/pred_0.jpg'.format(filename.split('.')[0]))

        return render_template('success.html', filename=output_path)

    return 'Invalid file! Allowed file types are: {}'.format(', '.join(app.config['ALLOWED_EXTENSIONS']))

# @app.route('/download/<filename>')
# def download(filename):
#     return send_from_directory('traffic/source/output'  , filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
