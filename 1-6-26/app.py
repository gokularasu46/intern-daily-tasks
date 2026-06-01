from flask import Flask, send_from_directory
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=None)

@app.route('/')
def index():
    return send_from_directory(ROOT_DIR, 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    target = os.path.join(ROOT_DIR, path)
    if os.path.isfile(target):
        return send_from_directory(ROOT_DIR, path)
    return send_from_directory(ROOT_DIR, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
