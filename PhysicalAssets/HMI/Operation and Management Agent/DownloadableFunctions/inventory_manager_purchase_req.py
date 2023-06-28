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
    performative_types = 'request_purchase_requirement'
    return {'Function Type':function_type,'Dependant Function':dependant_functions, 'active_passive' : active_passive, "performative_types": performative_types}

def execute():
    return purchase_alldetails()

def purchase_alldetails():
    reply_json = {}
    for root, dirs, files in os.walk("C:\\Users\\ashut\\OneDrive\\Desktop\\Custom Function Integration\\Machine_Twin 1", topdown=False):
        #print(root)
        for name in files:
            if name == 'rawmaterials.xlsx':
                fileraw = pd.read_excel(os.path.join(root,name))
                fileraw_val = fileraw[fileraw['quantity-available']<fileraw['quantity-required']]
                print(fileraw_val)
                root1 = os.path.dirname(root)
                root2 = os.path.dirname(root1)
                twinName = os.path.basename(root2)
                if twinName not in reply_json:
                    reply_json[twinName] = []
                #reply_json[twinName].append(fileraw_val)
                fileraw_val = fileraw_val.reset_index()
                for index, row in fileraw_val.iterrows():
                    reply_json[twinName].append({"Material_Code":row['material-code'],
                                                 "Material_Name":row['name'],
                                                 "Availabe_Quantity":row['quantity-available'],
                                                 "Minimum_Required":row['quantity-required']})

    return reply_json
#print(execute())
