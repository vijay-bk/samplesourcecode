from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure a secret key to use sessions (for demo purposes)
app.secret_key = 'your_secret_key'

# Configure a directory to store uploaded files
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    # If user does not select a file, browser also submits an empty part without filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        # Save the file to the uploads directory
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        return jsonify({'message': 'File successfully uploaded', 'filename': filename}), 200


if __name__ == '__main__':
    app.run(debug=True)
