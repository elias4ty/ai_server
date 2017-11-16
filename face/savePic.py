from flask import Flask,request
from werkzeug import secure_filename
import os,json,sys
from config import dic


app = Flask(__name__)

@app.route('/savePic/',methods=['POST'])
def save():

    SAVE_DIC = dic(sys.argv[1])
    PROXY_DIC = '/ai_resource/face/input/'

    file = request.files['picture']

    if file:
        filename = secure_filename(file.filename)
        urlPath = os.path.join(PROXY_DIC,filename)
        savePath = os.path.join(SAVE_DIC,filename)
        print(urlPath)
        file.save(savePath)

    _req = {
        'status' : 200,
        'url' : urlPath,
        'message' : 'suc'
    }

    return json.dumps(_req)

if __name__ == '__main__':
        app.run(host='0.0.0.0'
                ,debug = True)
