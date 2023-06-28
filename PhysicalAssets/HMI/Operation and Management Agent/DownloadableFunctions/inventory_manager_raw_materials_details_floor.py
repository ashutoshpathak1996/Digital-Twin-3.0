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
    performative_types = 'request_rawmaterial_detail_floor'
    return {'Function Type':function_type,'Dependant Function':dependant_functions, 'active_passive' : active_passive, "performative_types": performative_types}

def execute():
    return rawmaterial_floor_alldetails()

def rawmaterial_floor_alldetails():
    reply_json = {}
    for root, dirs, files in os.walk("C:\\Users\\ashut\\OneDrive\\Desktop\\Custom Function Integration\\Machine_Twin 1", topdown=False):
        for name in files:
            if name == 'rawmaterials.xlsx':
                fileraw = pd.read_excel(os.path.join(root,name))
                with open(os.path.join(root,'binconfig.txt')) as f:
                    binno = str(f.read())
                #print(binno)
                with open(os.path.join(root,'floorIDconfig.txt')) as f:
                    floorno = str(f.read())
                print(floorno)
                root1 = os.path.dirname(root)

                root2 = os.path.dirname(root1)
                twinName = os.path.basename(root2)
                if floorno not in reply_json:
                    reply_json[floorno] = []

                # reply_json[twinName].append(fileraw_val)
                fileraw_val = fileraw.reset_index()
                for index, row in fileraw_val.iterrows():
                    count = False
                    for items in reply_json[floorno]:
                        if items["Material_Code"] == row['material-code']:
                            count = True
                            items["Availabe_Quantity"] = items["Availabe_Quantity"] + row['quantity-available']
                            items["Minimum_Required"] = items["Minimum_Required"] + row['quantity-required']

                            break
                    if count == False:
                        reply_json[floorno].append({"Material_Code": row['material-code'],
                                                 "Material_Name": row['name'],
                                                 "Availabe_Quantity": row['quantity-available'],
                                                 "Minimum_Required": row['quantity-required']})

    return reply_json
#print(execute())
