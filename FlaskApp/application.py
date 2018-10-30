"""
    Module: application.py
    Last Update: 27 October 2018
"""

from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from database import execute_query
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['DEBUG'] = True
socketio = SocketIO(app)

users = {}

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
        username = request.form['username'] 
        password = request.form['password']
        print username, password
        """
            register username and password in the MySQL database
        """
	registration_query = "insert into users (username, password) values ('{}', '{}');".format(username, password)
        execute_query(registration_query)
        print "Registration Successful!"
        return render_template('login.html')
    else:
        return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """                                                                                                                                                                                                    
        The variables username and password                                                                                                                                                                
        are defined in registration.html                                                                                                                                                                   
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        login_query = "select * from users where username = '{}' and password= '{}'".format(username, password)
	results = execute_query(login_query)

	if len(results) > 0:
            print "Login Successful"
            return render_template("send_message.html", name=username)
        else:
            print "Login Failed!!!"
    else:
        
        return render_template('login.html')
        
@socketio.on('addUser', namespace='/login')
def add_user(data):
    session_id = request.sid
    users[data['username']] = session_id

@socketio.on('messageFromUser', namespace='/login')
def route_message(data):
    print('Message: {} From: {} To: {}'.format(data['message'], data['from_user'], data['to_user']))
    if data['to_user'] == 'all':
        emit('messageFromServer', data, broadcast=True, namespace='/login')
    else:
        to_session_id = users[data['to_user']]
	emit('messageFromServer', data, room=to_session_id, namespace='/login')

if __name__ == '__main__':
        socketio.run(app)

"""
References:
- https://stackoverflow.com/questions/42018603/handling-get-and-post-in-same-flask-view
- http://flask.pocoo.org/docs/1.0/quickstart/
- https://www.w3schools.com/tags/att_form_method.asp
- https://stackoverflow.com/questions/23989232/is-there-a-way-to-represent-a-directory-tree-in-a-github-readme-md
"""


