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
from DownloadableFunctions import *


### Watchdog for file changes
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# -----------------------------------------------------
parent_folder_path = os.getcwd()
function_pointing_table={}
function_pointing_table_file = open(parent_folder_path + r"\Application and Service Agent\FunctionPointingConfig.txt")
function_pointing_table_file_contents = function_pointing_table_file.read()
Lines = function_pointing_table_file_contents.splitlines()
for line in Lines:
    if line != "":
        key_values=line.split("=>")
        key=key_values[0]
        value=(key_values[1]).split("|")
        function_pointing_table[key] = value
#print(function_pointing_table)


function_available_table={}
function_available_table_file = open(parent_folder_path + r"\Application and Service Agent\AvailableFunctions.txt")
function_available_table_file_contents = function_available_table_file.read()
Lines = function_available_table_file_contents.splitlines()
for line in Lines:
    if line != "":
        key_values=line.split("=>")
        key=key_values[0]
        value=(key_values[1]).split("|")
        function_available_table[key] = value
##print(function_available_table)

ActiveFunctionsList = open(parent_folder_path + r"\Application and Service Agent\ActiveFunctionsList.txt")
ActiveFunctionsList_contents = ActiveFunctionsList.read()
Lines = ActiveFunctionsList_contents.splitlines()
for line in Lines:
    if line != "":
        key,value=line.split("=>")
        if value=='1':
            print(key)
            sys.path.append(parent_folder_path + r"\Application and Service Agent\DownloadableFunctions")
            import_module = __import__(key)
            thread=threading.Thread(target=import_module.Active)
            thread.start()

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
agent_id = 111111004
agent_ids = []
agent_name = 'as-1'

agent_role = 'analytics_service'

paths_dictionary = {}
paths_dictionary['agent_functions_path'] = parent_folder_path + r'\Application and Service Agent\DownloadableFunctions'
paths_dictionary[
    'active_conversations_path'] = parent_folder_path + r"\Application and Service Agent\Conversation_Logs\active_conversations"
paths_dictionary[
    'ended_coversations_path'] = parent_folder_path + r"\Application and Service Agent\Conversation_Logs\ended_conversations"
paths_dictionary[
    'active_functions_configuration'] = parent_folder_path + r"\Application and Service Agent\active_functions_config.txt"
paths_dictionary['agents_directory'] = parent_folder_path + r"\Application and Service Agent\agents_directory"
paths_dictionary['database'] = parent_folder_path + r"\Application and Service Agent\DataBase"
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
client.connect((host, port))

def machine_alldetails(msg):
    # Reading PassiveFunctionsList.txt to decide what analytic function type to return on trigger from platform
    PassiveFunctionsList = open(parent_folder_path + r"\Application and Service Agent\PassiveFunctionsList.txt")
    PassiveFunctionsList_contents = PassiveFunctionsList.read()
    Lines = PassiveFunctionsList_contents.splitlines()
    for line in Lines:
        if line != "":
            key,value=line.split("=>")
            if value == msg.content:
                sys.path.append(parent_folder_path + r"\Application and Service Agent\DownloadableFunctions")
                import_module = __import__(key)
                reply_json = import_module.execute()
                meta_data = json.dumps(reply_json)
                break
            else:
                continue
    print(meta_data)
    reply_parameters = {}
    reply_parameters["reply_performative"] = 'query_ref'
    reply_parameters["reply_type"] = 'inform_machinedetails_req'
    reply_parameters["reply_content"] = meta_data
    #print(reply_parameters)
    reply = create_a_reply_to_send(msg, reply_parameters)
    client.sendall(flatten(reply))

def tool_alldetails(msg):
    # Reading PassiveFunctionsList.txt to decide what analytic function type to return on trigger from platform
    PassiveFunctionsList = open(parent_folder_path + r"\Application and Service Agent\PassiveFunctionsList.txt")
    PassiveFunctionsList_contents = PassiveFunctionsList.read()
    Lines = PassiveFunctionsList_contents.splitlines()
    for line in Lines:
        if line != "":
            key,value=line.split("=>")
            if value == msg.content:
                sys.path.append(parent_folder_path + r"\Application and Service Agent\DownloadableFunctions")
                import_module = __import__(key)
                reply_json = import_module.execute()
                meta_data = json.dumps(reply_json)
                break
            else:
                continue
    print(meta_data)
    reply_parameters = {}
    reply_parameters["reply_performative"] = 'query_ref'
    reply_parameters["reply_type"] = 'inform_tooldetails_req'
    reply_parameters["reply_content"] = meta_data
    #print(reply_parameters)
    reply = create_a_reply_to_send(msg, reply_parameters)
    client.sendall(flatten(reply))

def machine_alarms(msg):
    # Reading PassiveFunctionsList.txt to decide what analytic function type to return on trigger from platform
    PassiveFunctionsList = open(parent_folder_path + r"\Application and Service Agent\PassiveFunctionsList.txt")
    PassiveFunctionsList_contents = PassiveFunctionsList.read()
    Lines = PassiveFunctionsList_contents.splitlines()
    for line in Lines:
        if line != "":
            key,value=line.split("=>")
            if value == msg.content:
                sys.path.append(parent_folder_path + r"\Application and Service Agent\DownloadableFunctions")
                import_module = __import__(key)
                reply_json = import_module.execute()
                meta_data = json.dumps(reply_json)
                break
            else:
                continue
    print(meta_data)
    reply_parameters = {}
    reply_parameters["reply_performative"] = 'query_ref'
    reply_parameters["reply_type"] = 'inform_machinealarms_req'
    reply_parameters["reply_content"] = meta_data
    #print(reply_parameters)
    reply = create_a_reply_to_send(msg, reply_parameters)
    client.sendall(flatten(reply))

def tool_alarms(msg):
    # Reading PassiveFunctionsList.txt to decide what analytic function type to return on trigger from platform
    PassiveFunctionsList = open(parent_folder_path + r"\Application and Service Agent\PassiveFunctionsList.txt")
    PassiveFunctionsList_contents = PassiveFunctionsList.read()
    Lines = PassiveFunctionsList_contents.splitlines()
    for line in Lines:
        if line != "":
            key,value=line.split("=>")
            if value == msg.content:
                sys.path.append(parent_folder_path + r"\Application and Service Agent\DownloadableFunctions")
                import_module = __import__(key)
                reply_json = import_module.execute()
                meta_data = json.dumps(reply_json)
                break
            else:
                continue
    print(meta_data)
    reply_parameters = {}
    reply_parameters["reply_performative"] = 'query_ref'
    reply_parameters["reply_type"] = 'inform_toolalarms_req'
    reply_parameters["reply_content"] = meta_data
    #print(reply_parameters)
    reply = create_a_reply_to_send(msg, reply_parameters)
    client.sendall(flatten(reply))

def recommendation(msg):
    # Reading PassiveFunctionsList.txt to decide what analytic function type to return on trigger from platform
    PassiveFunctionsList = open(parent_folder_path + r"\Application and Service Agent\PassiveFunctionsList.txt")
    PassiveFunctionsList_contents = PassiveFunctionsList.read()
    Lines = PassiveFunctionsList_contents.splitlines()
    for line in Lines:
        if line != "":
            key,value=line.split("=>")
            if value == msg.content:
                sys.path.append(parent_folder_path + r"\Application and Service Agent\DownloadableFunctions")
                import_module = __import__(key)
                reply_json = import_module.execute()
                meta_data = json.dumps(reply_json)
                break
            else:
                continue
    print(meta_data)
    reply_parameters = {}
    reply_parameters["reply_performative"] = 'query_ref'
    reply_parameters["reply_type"] = 'inform_recommendation_req'
    reply_parameters["reply_content"] = meta_data
    #print(reply_parameters)
    reply = create_a_reply_to_send(msg, reply_parameters)
    client.sendall(flatten(reply))

# ----------------------------------------------------------------------------------------- #
#                 Main Agent message handlers and response generation functions             #
# ----------------------------------------------------------------------------------------- #

def receive():
    while True:
        # try:
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

                    if msg.content == 'request_machine_report':
                        machine_alldetails(msg)
                    if msg.content == 'request_tool_report':
                        tool_alldetails(msg)
                    if msg.content == 'request_machine_alarm':
                        machine_alarms(msg)
                    if msg.content == 'request_tool_alarm':
                        tool_alarms(msg)
                    if msg.content == 'request_recommendation':
                        recommendation(msg)


        # except:
        #     print("an error occurred")
        #     client.close()
        #     break


#receive_thread = threading.Thread(target=receive)

#receive_thread.start()

