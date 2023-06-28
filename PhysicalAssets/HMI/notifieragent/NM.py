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

import json
### Watchdog for file changes
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# -----------------------------------------------------
parent_folder_path = os.getcwd()
function_pointing_table={}
function_pointing_table_file = open(parent_folder_path + r"\notifieragent\FunctionPointingConfig.txt")
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
function_available_table_file = open(parent_folder_path + r"\notifieragent\AvailableFunctions.txt")
function_available_table_file_contents = function_available_table_file.read()
Lines = function_available_table_file_contents.splitlines()
for line in Lines:
    if line != "":
        key_values=line.split("=>")
        key=key_values[0]
        value=(key_values[1]).split("|")
        function_available_table[key] = value
##print(function_available_table)

ActiveFunctionsList = open(parent_folder_path + r"\notifieragent\ActiveFunctionsList.txt")
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
agent_id = 111111009
agent_ids = []
agent_name = 'na-1'

agent_role = 'inventory_manager'

parent_folder_path = os.getcwd()
paths_dictionary = {}
paths_dictionary['agent_functions_path'] = parent_folder_path + r'\notifieragent\DownloadableFunctions'
paths_dictionary[
    'active_conversations_path'] = parent_folder_path + r"\notifieragent\Conversation_Logs\active_conversations"
paths_dictionary[
    'ended_coversations_path'] = parent_folder_path + r"\notifieragent\Conversation_Logs\ended_conversations"
paths_dictionary[
    'active_functions_configuration'] = parent_folder_path + r"\notifieragent\active_functions_config.txt"
paths_dictionary['agents_directory'] = parent_folder_path + r"\notifieragent\agents_directory"
paths_dictionary['database'] = parent_folder_path + r"\notifieragent\DataBase"
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

def tool_inspection(msg):
    reply_json = []
    for root, dirs, files in os.walk("..", topdown=False):
        for name in files:
            #print(name[-5:])
            if name[-5:] == '.json':
                with open(os.path.join(root,name)) as f:
                    try:
                        data = json.load(f)
                    except:
                        continue
                try:
                    twin_id = data['agent_id']
                    print(twin_id)
                    print(msg.content)
                    if twin_id == int(msg.content):
                        twinName = os.path.basename(root)
                        extrapath = r"\notifieragent\DataBase\Tool_inspection\tool_data.xlsx"
                        rootpath = os.path.abspath(root)
                        path = rootpath + extrapath
                        #print(path)
                        fileraw_val = pd.read_excel(path)
                        #print(fileraw_val)
                        fileraw_val = fileraw_val.reset_index()
                        for index, row in fileraw_val.iterrows():
                            reply_json.append(
                                {
                                    "name": row['name'],
                                    "date": str(row["date"].to_pydatetime().date()),
                                    "runtime": row["runtime"],
                                    "avg_velocity":row["avg_velocity"]

                                }
                            )
                        print(reply_json)
                        meta_data = json.dumps(reply_json)
                        print(meta_data)
                        reply_parameters = {}
                        reply_parameters["reply_performative"] = 'query_ref'
                        reply_parameters["reply_type"] = 'inform_sp_req'
                        reply_parameters["reply_content"] = meta_data
                        reply = create_a_reply_to_send(msg, reply_parameters)
                        client.sendall(flatten(reply))
                        break
                except:
                    continue

                #print(name)
#tool_inspection('hi')
def coolant_monitoring(msg):
    reply_json = []
    for root, dirs, files in os.walk("..", topdown=False):
        for name in files:
            # print(name[-5:])
            if name[-5:] == '.json':
                with open(os.path.join(root, name)) as f:
                    try:
                        data = json.load(f)
                    except:
                        continue
                try:
                    twin_id = data['agent_id']
                    #print(twin_id)
                    print(msg.content)
                    if twin_id == int(msg.content):
                        twinName = os.path.basename(root)

                        extrapath = r"\notifieragent\DataBase\Coolant_monitoring\coolant_data.xlsx"
                        rootpath = os.path.abspath(root)
                        path = rootpath + extrapath
                        print(path)
                        fileraw_val = pd.read_excel(path)
                        print(fileraw_val)
                        fileraw_val = fileraw_val.reset_index()
                        for index, row in fileraw_val.iterrows():
                            print(row["name"])
                            print(str(row["date"].to_pydatetime().date()))
                            print(str(row["time"]))
                            reply_json.append(
                                {
                                    "name": row["name"],
                                    "date": str(row["date"].to_pydatetime().date()),
                                    "time": str(row["time"]),
                                    "density": row["density"],
                                    "viscocity": row["viscocity"],
                                    "temperature": row["temperature"],

                                }
                            )
                        print(reply_json)
                        meta_data = json.dumps(reply_json)
                        print(meta_data)
                        reply_parameters = {}
                        reply_parameters["reply_performative"] = 'query_ref'
                        reply_parameters["reply_type"] = 'inform_sp_req'
                        reply_parameters["reply_content"] = meta_data
                        reply = create_a_reply_to_send(msg, reply_parameters)
                        client.sendall(flatten(reply))
                        break
                except:
                    continue
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

                    if msg.type == 'Tool_Inspection':
                        #print('hello')
                        tool_inspection(msg)
                    if msg.type == 'Coolant Monitoring':
                        coolant_monitoring(msg)


        # except:
        #     print("an error occurred")
        #     client.close()
        #     break


#receive_thread = threading.Thread(target=receive)

#receive_thread.start()

