
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
