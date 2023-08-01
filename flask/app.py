import os
from flask import Flask, flash, request, redirect, url_for, render_template, abort
from werkzeug.utils import secure_filename
from flask import send_from_directory
import cwe_cve_to_techniques
#import asyncio
import threading
import shutil

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {'json', 'txt', 'py'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#temp
app.secret_key = 'my-secret-key'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        ctrl_file = request.files["control_file"]
        vul_file = request.files["vul_file"]

        if ctrl_file.filename == '':
            flash('Error: Please Upload a Control File.')
            return redirect(request.referrer)
            # flash('No selected control file')
            # return redirect(request.url)
        elif vul_file.filename == '':
            flash('Error: Please Upload a Vulnerability File.')
            return redirect(request.referrer)
        # else:
        #if allowed_file(ctrl_file.filename) and allowed_file(vul_file.filename):
        ctrl_filename = 'in_' + ctrl_file.filename
        vul_filename = 'in_' + vul_file.filename
        
        ctrl_file.save(os.path.join(app.config['UPLOAD_FOLDER'], ctrl_filename))
        shutil.copyfile('./uploads/' + ctrl_filename, './uploads/controls.json')

        vul_file.save(os.path.join(app.config['UPLOAD_FOLDER'], vul_filename))
        shutil.copyfile('./uploads/' + vul_filename, './uploads/vulnerabilities.json')
            #control = open('./uploads/input.txt', 'w')


        # # check if the post request has the file part
        # if 'file' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        # files = request.files.getlist('file')
        #  # If the user does not select a file, the browser submits an
        # # empty file without a filename.
        # for file in files:
        #     print("NAME:", file.filename)
        #     if file.filename == '':
        #         flash('No selected file')
        #         return redirect(request.url)
        #     if file and allowed_file(file.filename):
        #         filename = secure_filename(file.filename)
        #         print('PAssed:', os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # NOTE: added
        #user_tactic = request.form.get("tactic_id")
        file = open('./uploads/input.txt', 'w')
        file.write('TA00' + request.form.get("tactic_id"))
        file.close()
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
