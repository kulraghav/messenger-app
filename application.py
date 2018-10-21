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

@app.route('/', methods=['GET'])
def index():
        return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
        The variables username and password 
        are defined in registration.html
    """
    if request.method == 'POST':
        username = request.values.get('username') 
        password = request.values.get('password')
        """
            register username and password in the MySQL database
        """
        return "<h1>Sent! Registration: Under Construction</h1>"
        pass
    else:
        return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """                                                                                                                                                                                                     
        The variables username and password                                                                                                                                                                 
        are defined in registration.html                                                                                                                                                                    
    """
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        """                                                                                                                                                                                                 
            login with username and password                                                                                                                                            
        """
        return "<h1>Sent! Login: Under Construction</h1>"
        pass
    else:
        return render_template('login.html')

if __name__ == '__main__':
        socketio.run(app)

"""
https://stackoverflow.com/questions/42018603/handling-get-and-post-in-same-flask-view

https://www.w3schools.com/tags/att_form_method.asp
"""
