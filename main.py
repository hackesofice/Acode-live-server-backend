from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from jinja2 import Environment, FileSystemLoader
from modules.port import get_available_port
#from modules.updater import updaterMethods
from modules.logo import showLogo
from appHandler import appHandler
import os

appHandler.startHandling()
showLogo()
app = Flask(__name__)
CORS(app)
portList = [1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034]
port = get_available_port(portList)
jsonData = {}
BASE_DIR = None
template_env = None

@app.route('/', methods=['GET', 'POST'])
def home():
    global template_env
    if request.method == 'GET':
        file_name = jsonData.get('fileName')
        if file_name and template_env:
            template = template_env.get_template(file_name)
            return template.render()
        else:
            return 'Template not configured.', 400
    else:
        return jsonify({"message": 'Hello, World!'}), 200

@app.route('/setup', methods=['PATCH'])
def setup():
    global BASE_DIR, jsonData, template_env
    data = request.get_json()
    file_name = data.get('fileName')
    path = data.get('path')

    if not file_name or not path:
        return jsonify({'error': 'fileName and path are required'}), 400

#    pathList = path.rsplit('/', 1)
#    if len(pathList) != 2:
#        return jsonify({'error': 'Invalid path format'}), 400

#    BASE_DIR = pathList[0]
#    template_folder = os.path.join(BASE_DIR, pathList[1])
    template_folder = path
    BASE_DIR = path
    if not os.path.isdir(template_folder):
        return jsonify({'error': 'Invalid template path'}), 400

    jsonData['fileName'] = file_name
    template_env = Environment(loader=FileSystemLoader(template_folder), auto_reload=True)

    return jsonify({'message': 'Base and template path set successfully'}), 201

#@app.route('/static/<path:filename>')
#def serve_static_file(filename):
  #  if not BASE_DIR:
 #       return 'Base directory not set.', 400
   # return send_from_directory(BASE_DIR, filename)
@app.route('/<path:filepath>')
def catch_all(filepath):
    global BASE_DIR
    DIR = BASE_DIR # getting a instance ig original path to make that gkobal variable uncahnged
    if not DIR:
        return 'BASE_DIR not set.', 400


   # if '.' in filepath:
   #     totalDots = filepath.count('.')
   #     DIR = (DIR.split('/'))[:-totalDots]
   #     DIR = '/'.join(DIR)
   #     filepath = filepath.replace('.', '')


    if filepath.startswith('.'):
        slashIndex = filepath.find("/")
        totalDots = filepath[:slashIndex].count('.')
        newPath = filepath[slashIndex:]
        DIR = (DIR.split('/'))[:-totalDots]
        DIR = '/'.join(DIR)
        filepath = newPath



                                                                                                                                              
    print('im hear boss')
    print(DIR)
    print(filepath)
    print(os.path.join(DIR, filepath))
    # Absolute path of the requested file
    file_path = os.path.join(DIR, filepath)

    if os.path.isfile(file_path):
        return send_file(file_path)
    else:
        return f'File not found: {filepath}', 404

@app.route('/check', methods=["GET"])
def send_alive_signal_too_the_client():
  if request.method == "GET":
    print("Successfully Port Identified by the client connection process started")
    return jsonify({"message":"Ready For 'PATCH' request","key":"AcodeLiveServer","port": f"{port}"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)


