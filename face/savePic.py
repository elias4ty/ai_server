from flask import Flask,request
from werkzeug import secure_filename
import os,json,sys


app = Flask(__name__)

@app.route('/savePic/',methods=['POST'])
def save():
    DIC = '/Users/elias/Documents/python_exercise/flask_01'

    file = request.files['picture']
    print(sys.path)
    if file:
        filename = secure_filename(file.filename)
        urlPath = os.path.join(DIC,filename)
        print(urlPath)
        file.save(urlPath)

    _req = {
        'status' : 200,
        'url' : urlPath,
        'message' : 'suc'
    }

    return json.dumps(_req)

if __name__ == '__main__':
        app.run(host='0.0.0.0'
                ,debug = True)
