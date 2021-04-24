from flask import Flask, render_template, request
from threading import Thread


app = Flask('')


@app.route("/", methods=["GET"])

def index():
    return render_template('index.html')

def get_my_ip():
    x = request.remote_addr
    file = open('text.log', 'a')
    file.write(f'{x}\n')
    return x

def run():
    app.run(host="0.0.0.0", port="6969")

def keep_alive():
    server = Thread(target=run)
    server.start()
