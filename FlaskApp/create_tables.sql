CREATE TABLE users (                                                                                                                                                                                        
   user_id int(8),                                                                                                                                                                                          
   username varchar(255),                                                                                                                                                                                   
   password varchar(255)                                                                                                                                                                                    
                                                                                                                                                                                                            
);                                                                                                                                                                                                          
                                                                                                                                                                                                            
CREATE TABLE chats (                                                                                                                                                                                        
   chat_id int(8),                                                                                                                                                                                          
   text  varchar(255),                                                                                                                                                                                     

   from_uid int(8),                                                                                                                                                                                         
   to_uid int(8),                                                                                                                                                                                           
   created_at timestamp                                                                                                                                                                                     
);      
