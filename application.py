"""
    Module: application.py
    Last Update: 21 October 2018
"""


from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['DEBUG'] = True
socketio = SocketIO(app)

@app.route('/')
def index():
        return render_template('index.html')

if __name__ == '__main__':
        socketio.run(app)

