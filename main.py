
from flask import Flask, request, send_from_directory

from os import mkdir, environ
from os.path import exists, join
import uuid

UPLOAD_FOLDER = environ.get('IMAGE_UPLOAD_PATH')

app = Flask(__name__)


if not exists(UPLOAD_FOLDER):
    mkdir(UPLOAD_FOLDER)

@app.route('/<path:path>', methods=['GET'])
def send(path):
    return send_from_directory(UPLOAD_FOLDER, path)

@app.route('/', methods=['POST'])
def upload_file():
    image = request.files['image']
    filename = f"{str(uuid.uuid4())}.{image.filename.split('.')[-1]}"
    path = join(UPLOAD_FOLDER, filename)
    image.save(path)
    return { 'image_path': filename }


if __name__ == '__main__':
    app.run(host=environ.get('FLASK_RUN_HOST'))
