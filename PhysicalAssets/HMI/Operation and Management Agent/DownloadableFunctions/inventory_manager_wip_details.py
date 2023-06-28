import json
import sys
import csv
import pandas as pd
import datetime
import os


def introduction():
    function_type = 'InventoryManager'
    dependant_functions = []
    active_passive = 'Passive'
    performative_types = 'request_wip_details'
    return {'Function Type':function_type,'Dependant Function':dependant_functions, 'active_passive' : active_passive, "performative_types": performative_types}

def execute():
    return wip_alldetails()

def wip_alldetails():
    reply_json = []
    for root, dirs, files in os.walk("C:\\Users\\ashut\\OneDrive\\Desktop\\Custom Function Integration\\Machine_Twin 1", topdown=False):
        #print(root)
        for name in files:
            if name == 'wip.xlsx':
                fileraw_val = pd.read_excel(os.path.join(root,name))
                reply_dict = {}
                #print(fileraw_val)
                root1 = os.path.dirname(root)
                root2 = os.path.dirname(root1)
                with open(os.path.join(root,'floorIDconfig.txt')) as f:
                    floorno = str(f.read())
                twinName = os.path.basename(root2)
                reply_dict["twinName"] = twinName
                reply_dict["floorno"] = floorno
                reply_dict["underprocess"] = []
                reply_dict["waiting"] = []
                #reply_json[twinName].append(fileraw_val)
                fileraw_val = fileraw_val.reset_index()
                for index, row in fileraw_val.iterrows():
                    if row["status"] == "underprocess":
                        reply_dict["underprocess"].append(row["job-id"])
                    else:
                        reply_dict["waiting"].append(row["job-id"])

                reply_json.append(reply_dict)
                
    return reply_json
#print(execute())
