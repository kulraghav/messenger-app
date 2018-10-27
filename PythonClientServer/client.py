import sys
import socket
import select

def chat_client():
    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(2)

    # connect to remote host                                                                                                                                                                                
    try :
        client_socket.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()

    print 'Connected to remote host. You can start sending messages'
    sys.stdout.write('[Me] '); sys.stdout.flush()

    while 1:
        sockets = [sys.stdin, client_socket]

        # Get the list sockets which are readable                                                                                                                                                           
        read_sockets, write_sockets, in_error = select.select(sockets , [], [])

        for sock in read_sockets:
            if sock == client_socket:
                # incoming message from remote server, s                                                                                                                                                    
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #print data                                                                                                                                                                             
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] '); sys.stdout.flush()

            else :
                # user entered a message                                                                                                                                                                    
                message = sys.stdin.readline()
                
                client_socket.send(message)
                sys.stdout.write('[Me] '); sys.stdout.flush()

if __name__ == "__main__":

    sys.exit(chat_client())
