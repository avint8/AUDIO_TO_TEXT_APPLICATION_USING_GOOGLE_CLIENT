from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":

        files=request.files['audio_data']
        files.save('file.wav')


        



    return render_template("index.html")

if __name__ == "__main__":
    app.run()