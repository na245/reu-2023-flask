import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
import cwe_cve_to_techniques
#import asyncio
import threading

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {'json', 'txt', 'py'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('file')
         # If the user does not select a file, the browser submits an
        # empty file without a filename.
        for file in files:
            print("NAME:", file.filename)
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print('PAssed:', os.path.join(app.config['UPLOAD_FOLDER'], filename))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	    
        return redirect(url_for('result'))
    return render_template('index.html')


# @app.route('/templates/test')
# def test():
#     return render_template('test.html')

@app.route('/templates/table')
def table():
    return render_template('table.html')

@app.route('/templates/network_flow')
def network_flow():
    return render_template('network_flow.html')

@app.route('/templates/result', methods=['GET', 'POST'])
def result():
    x = threading.Thread(target=cwe_cve_to_techniques.main)
    x.start()
    x.join()
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()
    return render_template('result.html')

@app.route('/templates/graph')
def graph():
    return render_template('graph.html')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
