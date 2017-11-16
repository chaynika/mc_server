from flask import Flask
from flask import request
import pdb
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #print(request.__dict__)
        f = request.files['files']
        print(f.filename)
        filename = '/Users/csaikia/Dropbox/Coursework/CSE535/uploaded_files/'+f.filename
        f.save(filename)
        return '200'
    else:
        return 'Upload Page'

if __name__ == '__main__':
    app.debug = True
    app.run()

