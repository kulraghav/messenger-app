
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
    * send_message.html (chat history and a text-box to send message)
   

* Back-end (python + flask)
    * application.py (flask application using socket.io)
    * login.py (login related functionalities)
    * registration.py (registration related functionalities)
    * database.py (database related functionalities)

* Folder structure
$ tree

```bash
.
├── README.md
├── application.py
├── create_tables.sql
├── database.py
├── login.py
├── registration.py
└── templates
    ├── chat_history.html
    ├── index.html
    ├── login.html
    ├── registration.html
    ├── send_message.html
    └── users.html

1 directory, 12 files
'''

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

