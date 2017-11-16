from flask import Flask,request
from werkzeug import secure_filename
import os,json,sys
from config import dic
# sys.path.append('/home/ai_demo/mtcnn')
# from demo import main

app = Flask(__name__)


@app.route('/',methods=['POST'])
def hello():

    filename = request.form['filename'];

    main(filename)

    result = {
        'status' : 200,
        'message' : 'OK',
        'url' : '/ai_resource/face/output/'+filename
    }

    return json.dumps(result)

@app.route('/savePic/',methods=['POST'])
def save():

    SAVE_DIC = dic(sys.argv[1])
    PROXY_DIC = '/ai_resource/face/input/'

    file = request.files['picture']

    if file:
        filename = secure_filename(file.filename)
        urlPath = os.path.join(PROXY_DIC,filename)
        savePath = os.path.join(SAVE_DIC,filename)
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
