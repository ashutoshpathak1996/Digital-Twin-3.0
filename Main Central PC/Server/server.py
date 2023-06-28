import json
import socket
import threading
from BaseLibraries.messaging import flatten, unflatten
from BaseLibraries.messaging import dummyFIPA
import time
import os

parent_dir=os.getcwd()
with open(parent_dir+r'\server_ip.txt') as f:
    lines=[]
    for line in f.readlines():
        lines.append(line)
    port = int(lines[0])
    host = lines[1]
    f.close()
#host = 'localhost'  
#port = 85

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()  # server start listening for connections

clients = []
agent_ids = []


# broadcasting message to all the clients
def broadcast(message):
    for client in clients:
        client.sendall(message)


def forward_to_receivers(message):
    msg = unflatten(message)


    #print(msg) #line for debug
    print(f"sending {msg.performative} from {msg.sender} to {int(msg.receiver)}")
    if msg.protocol != "DUMMY_FIPA":
        try: #One change in msg.receiver int
            for n_name in eval(int(msg.receiver)):

                agentid_index = agent_ids.index(n_name)
                clients[agentid_index].sendall(message)
                time.sleep(0.5)
        except:
            agentid_index = agent_ids.index(int(msg.receiver))
            clients[agentid_index].sendall(message)
            time.sleep(0.5)


def handle(client):
    print("initial tasks done")
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = bytes(message)
                while len(message) > 1023:
                    message = client.recv(1024)
                    #print(message)
                    #print(msg)
                    msg += message

                msg = unflatten(msg)
                print(msg)
                if msg.content == "platform_disconnection":
                    print('hel')
                    try:

                        index = clients.index(client)
                        agent_id = agent_ids[index]
                        broadcast(flatten(dummyFIPA("client_disconnected", agent_id)))
                        print(f"{agent_id} got disconnected")
                        while True:
                            index = agent_ids.index(agent_id)
                            client = clients[index]
                            agent_ids.remove(agent_id)
                            #print(agent_ids)
                            clients.remove(client)
                            client.close()
                            print(clients)



                    except:

                        break
                else:
                    # broadcast(message)
                    msg = flatten(msg)
                    forward_to_receivers(msg)

        except:
            # if no such message is recieved
            # we terminate the client and
            # broadcast that the client has
            # left the chat
            index = clients.index(client)
            agent_id = agent_ids[index]
            #broadcast(flatten(dummyFIPA("client_disconnected",agent_id)))
            print(f"{agent_id} got disconnected")
            agent_ids.remove(agent_id)
            clients.remove(client)
            client.close()
            break

def recieve():
    print("server is listening...")
    while True:
        client, address = server.accept()
        # printing on the server the
        # notification of new connection
        print(f"connected with {str(address)}")

        # getting the agent_id from the client
        # by sending them the codeword NICK

        client.sendall(flatten(dummyFIPA("server_topics", 'NICK')))
        agent_id = unflatten(client.recv(1024)).content
        print(agent_id)

        # adding agent_id and client of the
        # client in the list

        agent_ids.append(agent_id)
        clients.append(client)
        client.sendall(flatten(dummyFIPA("active_agents", agent_ids)))

        # printing agent_id on server and broadcasting
        # the agent_id to all clients in chat
        print(f" name of the client is {agent_id}")
        broadcast(flatten(dummyFIPA("client_connected", agent_id)))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
#recieve()
