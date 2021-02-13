from flask import Flask, render_template, request, url_for, send_from_directory, jsonify
import os

app = Flask(__name__, static_folder="assets")
ROOT_DIR = os.getcwd()

@app.route('/')
def home():
    return render_template('models.html')

if __name__=="__main__":
    app.run(debug=True)