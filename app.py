from flask import Flask, render_template, request, jsonify, send_file
from steganography import embed_text, extract_text
import os

app = Flask(__name__)

# Folder to store processed images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/embed', methods=['POST'])
def embed():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided.'})

    image_file = request.files['image']
    secret_text = request.form['secret-text']
    key = int(request.form['key'])

    # Ensure the 'static/uploads' folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Generate a unique filename for the processed image
    result_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result_image.png')

    # Call the embed_text function to embed text
    embed_text(image_file, secret_text, result_image_path, key)

    # Send the filename back to the client
    filename = os.path.basename(result_image_path)
    return jsonify({'message': 'Text embedded successfully.', 'result_image_path': result_image_path, 'filename': filename})

@app.route('/extract', methods=['POST'])
def extract():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided.'})

    image_file = request.files['image']
    key = int(request.form['key'])

    # Call the extract_text function to extract text
    extracted_text = extract_text(image_file, key)

    return jsonify({'extracted_text': extracted_text})

@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)