from flask import Flask, jsonify
from flask import request
import pdb
#TODO Add import line for my comparator code package

app = Flask(__name__)

# Just for testing
@app.route('/')
def hello_world():
    return 'Hello World!'

# Upload file to server API
@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #print(request.__dict__)
        f = request.files['files']
        print(f.filename)
# TODO rename the file location to a train directory
        filename = '/Users/csaikia/Dropbox/Coursework/CSE535/uploaded_files/'+f.filename
        f.save(filename)
        return '200'
    else:
        return 'Upload Page'

@app.route('/compare_signature', methods = ['POST'])
def compare_signature():
    f = request.files['files']
    filename = '/Users/csaikia/Dropbox/Coursework/CSE535/uploaded_files/'+f.filename
    f.save(filename)
# TODO write comparator code
    #return_code = comparator.compare(f.filename)
    return_code = 1
    return jsonify(exit_code = return_code)

if __name__ == '__main__':
    app.debug = True
    app.run()

