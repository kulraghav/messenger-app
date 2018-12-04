CREATE TABLE IF NOT EXISTS users (                                                                                                                                                                                        
   user_id int(8) NOT NULL AUTO_INCREMENT,                                                                                                                                                                                          
   username varchar(255),
   password varchar(255),
   PRIMARY KEY (user_id)                                                                                                                                                                            
);

CREATE TABLE IF NOT EXISTS chats (                                                                                                                                                                                        
   chat_id int(8) NOT NULL AUTO_INCREMENT,
   text  varchar(255),
   from_uid int(8),
   to_uid int(8),
   created_at timestamp,
   PRIMARY KEY (chat_id)
);