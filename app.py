from flask import Flask, request, render_template
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded", 400
        file = request.files['file']
        if file.filename == '':
            return "No file selected", 400
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        # Изменение размера изображения
        img = Image.open(filepath)
        img = img.resize((200, 200))
        img.save(filepath)
        return render_template('result.html', filename=file.filename)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)