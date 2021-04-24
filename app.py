from flask import Flask, render_template, request, jsonify
from threading import Thread

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port="6969")
