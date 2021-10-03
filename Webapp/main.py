#main.py
from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
from count_colonies import *
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("webpage.html")

@app.route('/myform.cgi', methods=['POST'])
def count():
    print("okayyyy")
    uploaded_file = request.files['fileupload']
    if uploaded_file.filename != '':
        img = preprocess(uploaded_file)
        nbr_colonies = count_colonies(np.asarray(img))
        print(nbr_colonies)
        uploaded_file.save("templates/image.jpg")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    print("test")