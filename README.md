
# Chat Messenger

## Usage
* Download the folder messenger-app
* Run the web-app using the following command from folder messenger-app: 
    * python application.py
* Access the web-app at: localhost:5000 (can also be deployed on AWS)

## Design

* Front-end (html + css + javascript) 
    * index.html (registration and login buttons)
    * registration.html (registration page)
    * login.html (login page)
    * users.html (list of users and their hyperlinks)
    * chat_history.html (chat history between two specified users)

* Back-end (python + flask)
    * application.py (flask application using socket.io)
    * login.py (login related functionalities)
    * registration.py (registration related functionalities)
    * database.py (database related functionalities)


## Database 
MySQL 
* Users
    * user_id
    * username
    * password

* Chats
    * chat_id
    * from_uid
    * to_uid
    * created_at
    * text


## Next:
- rooms (MongoDB)
- chat status
- user status
  

https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md  

