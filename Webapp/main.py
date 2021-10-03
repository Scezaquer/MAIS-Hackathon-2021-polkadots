#main.py
from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
from count_colonies import *
from segmentation import *
import numpy as np
import os
import base64
import io

app = Flask(__name__)
model = loadNN(path)

@app.route("/")
def index():
    return render_template("webpage.html")

@app.route('/myform.cgi', methods=['POST'])
def count():
    print("okayyyy")
    uploaded_file = request.files['fileupload']
    if uploaded_file.filename != '':
        im = Image.open(uploaded_file)
        im.thumbnail((400, 300))
        data = io.BytesIO()
        im.save(data, "JPEG")
        encoded_img_data = base64.b64encode(data.getvalue())

        #img = preprocess(img)
        nbr_colonies = count_colonies(Image.open(uploaded_file))
        #print(nbr_colonies)
    return render_template("result.html", count=nbr_colonies, img_data=encoded_img_data.decode('utf-8'))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    for x in os.listdir(app.config["UPLOAD_FOLDER"]):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], x))