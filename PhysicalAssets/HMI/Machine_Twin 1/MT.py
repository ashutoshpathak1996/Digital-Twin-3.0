import csv
import queue
import socket
import time
import os
import pandas as pd
import datetime
import pickle
# -----------------------------------------------------
import threading
from BaseLibraries.messaging import *
from BaseLibraries.support_files import *


### Watchdog for file changes
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# -----------------------------------------------------
parent_folder_path = os.getcwd()
function_pointing_table={}
function_pointing_table_file = open(parent_folder_path + r"\Machine_Twin 1\FunctionPointingConfig.txt")
function_pointing_table_file_contents = function_pointing_table_file.read()
Lines = function_pointing_table_file_contents.splitlines()
for line in Lines:
    if line != "":
        key_values=line.split("=>")
        key=key_values[0]
        value=(key_values[1]).split("|")
        function_pointing_table[key] = value
##print(function_pointing_table)


function_available_table={}
function_available_table_file = open(parent_folder_path + r"\Machine_Twin 1\AvailableFunctions.txt")
function_available_table_file_contents = function_available_table_file.read()
Lines = function_available_table_file_contents.splitlines()
for line in Lines:
    if line != "":
        key_values=line.split("=>")
        key=key_values[0]
        value=(key_values[1]).split("|")
        function_available_table[key] = value
##print(function_available_table)

ActiveFunctionsList = open(parent_folder_path + r"\Machine_Twin 1\ActiveFunctionsList.txt")
ActiveFunctionsList_contents = ActiveFunctionsList.read()
Lines = ActiveFunctionsList_contents.splitlines()
for line in Lines:
    if line != "":
        key,value=line.split("=>")
        if value=='1':
            print(key)
            string=key+"_thread=threading.Thread(target="+key+".Active).start()"
            print(string)
            exec(string)


# ===========================================================================================
#                           BEFORE CONTACTING SERVER
# =========================================================================================


# to create type to function mapping and function pointing files

msg_to_send_queue = queue.Queue()
timed_reply_queue = queue.Queue()
allotment_queue = queue.Queue()
parameters_queue = queue.Queue()


protocols_list = ['contract_net_interaction_protocol', 'request_interaction_protocol', 'request-when_interaction_protocol',
                  'query_interaction_protocol', 'broking_interaction_protocol',
                  'recruiting_interaction_protocol',
                  'propose interaction protocol', 'subscribe interaction protocol']

performatives_list = ['call_for_proposal','request', 'accept_proposal', 'agree', 'cancel',  'confirm',
                      'disconfirm', ' failure', 'inform', 'inform_if', 'inform-ref'
    , 'not_understood', 'propagate', 'propose', 'proxy', 'query_if',
                      'query_ref', 'refuse', 'reject_proposal', 'request_when'
                                                                'request_whenever', 'subscribe']

global agent_id
agent_id = 1001
agent_ids = []
agent_name = 'dt-1'

agent_role = 'twin'

paths_dictionary = {}
paths_dictionary['agent_functions_path'] = parent_folder_path + r'\Machine_Twin 1\DownloadableFunctions'
paths_dictionary[
    'active_conversations_path'] = parent_folder_path + r"\Machine_Twin 1\Conversation_Logs\active_conversations"
paths_dictionary[
    'ended_coversations_path'] = parent_folder_path + r"\Machine_Twin 1\Conversation_Logs\ended_conversations"
paths_dictionary[
    'active_functions_configuration'] = parent_folder_path + r"\Machine_Twin 1\active_functions_config.txt"
paths_dictionary['agents_directory'] = parent_folder_path + r"\Machine_Twin 1\agents_directory"
paths_dictionary['database'] = parent_folder_path + r"\Machine_Twin 1\DataBase"
paths_dictionary['agent_id'] = agent_id
paths_dictionary['agent_role'] = agent_role
paths_dictionary['agent_name'] = agent_name

create_mapping_and_pointing_files(paths_dictionary, msg_to_send_queue)
with open(parent_folder_path+r'\hmi_ip.txt') as f:
    lines=[]
    for line in f.readlines():
        lines.append(line)
    port = int(lines[0])
    host = lines[1]
    f.close()
global client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, 85))


## Platform specific internal function for agents who work as twin
def register_twin(msg):
    meta_filepath = parent_folder_path + r"\Machine_Twin 1\MachineCommunication\agent_metadata.json"
    with open(meta_filepath) as file:
        meta_data = json.load(file)
    meta_data = json.dumps(meta_data)
    reply_parameters = {}
    reply_parameters["reply_performative"] = 'query_ref'
    reply_parameters["reply_type"] = 'agreed'
    reply_parameters["reply_content"] = meta_data
    reply = create_a_reply_to_send(msg,reply_parameters)
    client.sendall(flatten(reply))





def connect_twin(msg):
    meta_filepath = parent_folder_path + r"\Machine_Twin 1\MachineCommunication\agent_metadata.json"
    folder_track = parent_folder_path + r"\Machine_Twin 1\MachineCommunication"

    def connectfunc():
        print(msg.sender)
        print(agent_ids)

        with open(meta_filepath) as file:
            meta_data = json.load(file)

        meta_data = json.dumps(meta_data)
        reply_parameters = {}
        reply_parameters["reply_performative"] = 'query_ref'
        reply_parameters["reply_type"] = 'agreed'
        reply_parameters["reply_content"] = meta_data
        reply = create_a_reply_to_send(msg, reply_parameters)
        client.sendall(flatten(reply))
        return


    connectfunc()
    while True:
        time.sleep(2)
        if msg.sender in agent_ids:
            a = connectfunc()
            time.sleep(2)

        else:
            break
    #     connectfunc()
    #     time.sleep(1)
    # class handler(FileSystemEventHandler):
    #     def on_modified(self, event):
    #         connectfunc()
    # observer = Observer()
    # event_handler = handler()
    # observer.schedule(event_handler,folder_track,recursive=True)
    # observer.start()
    #
    # while True:
    #     if msg.sender in agent_ids:
    #         time.sleep(1)
    #     else:
    #         observer.stop()
    #         break
    # observer.join()





    ## Before watchdog changes made
    # meta_filepath = parent_folder_path + r"\MachineCommunication\agent_metadata.json"
    #
    #
    # while True:
    #     print(msg.sender)
    #     print(agent_ids)
    #     if msg.sender in agent_ids:
    #         with open(meta_filepath) as file:
    #             meta_data = json.load(file)
    #         meta_data = json.dumps(meta_data)
    #         reply_parameters = {}
    #         reply_parameters["reply_performative"] = 'query_ref'
    #         reply_parameters["reply_type"] = 'agreed'
    #         reply_parameters["reply_content"] = meta_data
    #         reply = create_a_reply_to_send(msg, reply_parameters)
    #         client.send(flatten(reply))
    #         time.sleep(8)
    #     else:
    #         break
    # return


# ----------------------------------------------------------------------------------------- #
#                 Main Agent message handlers and response generation functions             #
# ----------------------------------------------------------------------------------------- #

def receive():
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(message)
                # if the server send a NICK then
                # we send the agent_id back
                if msg.protocol == "DUMMY_FIPA":
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", agent_id)))

                    elif msg.type == "client_connected":  # this message is only sent once by server at initiation

                        agent_ids.append(msg.content)


                    elif msg.type == "client_disconnected":

                        agent_id_index = agent_ids.index(msg.content)
                        try:
                            while True:
                                agent_ids.remove(msg.content)
                        except:
                            pass


                    elif msg.type == "active_agents":  # this message is only sent once by server at initiation
                        pass

                    else:
                        pass

                else:

                    print(f"{msg.performative} received ", "cid = ", msg.conversation_id)
                    #timed_reply_queue.put(msg)
                    #parentMessageHandler(msg)
                    if msg.performative == 'query_ref':
                        if msg.content == 'platform_registration':
                            register_twin(msg)
                        if msg.content == 'platform_connection':
                            thread = threading.Thread(target=connect_twin, args=(msg,))
                            thread.start()

        except:
            return
        #     print("an error occurred")
        #     client.close()
        #     break


# if message is getting printed twice, it is because
# sender is printing it, and same message is being received by receiver
# as stuff is broadcasted and that gets printed as well!!


# queues_thread = threading.Thread(target= print_on_GUI_and_send_from_queue, args = [msg_to_send_queue,])
#receive_thread = threading.Thread(target=receive)
#
# queues_thread.start()
#receive_thread.start()

