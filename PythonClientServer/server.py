import sys
import socket
import select

HOST = '' 
RECV_BUFFER = 4096 
PORT = 9009

sockets = []

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)

    # add server socket object to the list of readable connections
    sockets.append(server_socket)
    
    print "Chat server started on port " + str(PORT)

    while 1:
        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        read_sockets, write_sockets, in_error = select.select(sockets, [], [],0)
        for sock in read_sockets:
            # a new connection request recieved
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                sockets.append(sockfd)
                print "Client (%s, %s) connected" % addr
                 
                broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)
             
            # a message from a client, not a new connection
            else:
                # process data recieved from client, 
                try:
                    # receiving data from the socket.
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        # there is something in the socket
                        broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)  
                    else:
                        # remove the socket that's broken    
                        if sock in sockets:
                            sockets.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                        broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

                # exception 
                except:
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue

    server_socket.close()
    
# broadcast chat messages to all connected clients                                                                                                                                                          
def broadcast (server_socket, from_socket, message):
    for socket in sockets:
        # send the message only to peer                                                                                                                                                                     
        if socket != server_socket and socket != from_socket :
            try :
                socket.send(message)
            except :
                # broken socket connection                                                                                                                                                                  
                socket.close()
                # broken socket, remove it                                                                                                                                                                  
                if socket in sockets:
                    sockets.remove(socket)

if __name__ == "__main__":
    sys.exit(server())
