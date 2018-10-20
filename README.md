# Chat Messenger

- main file: application.py
- usage: 
>> python application.py
- access point: localhost:5000 (can also be deployed on AWS)

## Basic Design

- Front-end: (html + css + javascript) 
  index.html             registration and login buttons
  registration.html      registration page
  login.html             login page
  users.html             list of users and their hyperlinks
  chat_history.html      chat history between two specified users

- Back-end:
  application.py         flask application using socket.io
  login.py               login related functionalities
  registration.py        registration related functionalities
  database.py            database related functionalities


## Database Tables (MySQL)
- Users
  -- user_id
  -- username
  -- password

- Chats
  -- chat_id
  -- from_uid
  -- to_uid
  -- created_at
  -- text


### Later:
- rooms (MongoDB)
- chat status
- user status
    

