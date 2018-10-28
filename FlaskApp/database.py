
"""                                                                                                                                                                                                                                                                                                                                                                                                           
Module: Database (database.py)                                                                                                                                                                  
Usage:                                                                                                                                                                                                      
    Example 1:                                                                                                                                                                                              
    >> from database import execute_query                                                                                                                                                             
    >> my_query = "select id from users"                                                                                                                                                                    
    >> execute_query(my_query)                                                                                                                                                                              
                                                                                                                                                                                                            
Last Update: 21 October 2018                                                                                                                                                                                            
"""

import MySQLdb
import os

"""                                                                                                                                                                                                         
Hardwiring the configuration variables.                                                                                                                                           
"""

db_host = 'localhost'
db_user = 'root'
db_password = 'NewPassword'
db_name = 'messenger_app'

# this is to solve the unicode-decode problem                                                                                                                                                               
db_charset = "utf8"
db_use_unicode = True

db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name, charset=db_charset, use_unicode=db_use_unicode)


def execute_query(query):
    query = "".join(query.strip().split('\n'))
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.commit()
    return list(results)


"""
In [1]: from database import execute_query

In [2]: execute_query("show tables;")
Out[2]: [(u'chats',), (u'users',)]

"""

"""
mysql> create database messenger_app;                                                                                                                                                                       
Query OK, 1 row affected (0.02 sec)                                                                                                                                                                         
                                                                                                                                                                                                            
mysql> use messenger_app;                                                                                                                                                                                   
Database changed                                                                                                                                                                                            
                                                                                                                                                                                                            
CREATE TABLE users (                                                                                                                                                                                        
   user_id int(8),                                                                                                                                                                                          
   username varchar(255),                                                                                                                                                                                   
   password varchar(255)                                                                                                                                                                                    
);                                                                                                                                                                                                          
                                                                                                                                                                                                            
CREATE TABLE chats (                                                                                                                                                                                        
   chat_id int(8),                                                                                                                                                                                          
   text  varchar(255),                                                                                                                                                                                     \
   from_uid int(8),                                                                                                                                                                                         
   to_uid int(8),                                                                                                                                                                                           
   created_at timestamp                                                                                                                                                                                     
);      
"""


"""
mysql> show tables                                                                                                                                                                                          
    -> ;                                                                                                                                                                                                    
+-------------------------+                                                                                                                                                                                 
| Tables_in_messenger_app |                                                                                                                                                                                 
+-------------------------+                                                                                                                                                                                 
| chats                   |                                                                                                                                                                                 
| users                   |                                                                                                                                                                                 
+-------------------------+                                                                                                                                                                                 
                                                                                                                                                                                                            
mysql> show columns from users;                                                                                                                                                                             
+----------+--------------+------+-----+---------+-------+                                                                                                                                                  
| Field    | Type         | Null | Key | Default | Extra |                                                                                                                                                  
+----------+--------------+------+-----+---------+-------+                                                                                                                                                  
| user_id  | int(8)       | YES  |     | NULL    |       |                                                                                                                                                  
| username | varchar(255) | YES  |     | NULL    |       |                                                                                                                                                  
| password | varchar(255) | YES  |     | NULL    |       |                                                                                                                                                  
+----------+--------------+------+-----+---------+-------+                                                                                                                                                  
                                                                                                                                                                                                            
mysql> show columns from chats                                                                                                                                                                              
    -> ;                                                                                                                                                                                                    
+------------+--------------+------+-----+-------------------+-----------------------------+                                                                                                                
| Field      | Type         | Null | Key | Default           | Extra                       |                                                                                                                
+------------+--------------+------+-----+-------------------+-----------------------------+                                                                                                                
| chat_id    | int(8)       | YES  |     | NULL              |                             |                                                                                                                
| text       | varchar(255) | YES  |     | NULL              |                             |                                                                                                                
| from_uid   | int(8)       | YES  |     | NULL              |                             |                                                                                                                
| to_uid     | int(8)       | YES  |     | NULL              |                             |                                                                                                                
| created_at | timestamp    | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |                                                                                                                
+------------+--------------+------+-----+-------------------+-----------------------------+                                                                                                                
"""
