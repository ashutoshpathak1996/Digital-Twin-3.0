import random
import pandas as pd
import scipy.stats as stats
import numpy as np
import json
import sys
import os


parent_dir = os.getcwd()
def introduction():
    function_type = 'AlarmGeneration'
    dependant_functions = ['analytic_tool_condition']
    active_passive = 'Passive'
    performative_types = 'request_tool_alarm'
    return {'Function Type':function_type,'Dependant Function':dependant_functions, 'active_passive' : active_passive, "performative_types": performative_types}

def execute():
    return alarm_generation()

def alarm_generation():
    sys.path.append(parent_dir + r"\Application and Service Agent\DownloadableFunctions")
    x = introduction()
    #print(x["Dependant Function"])
    callable_Data=[]
    for i in x["Dependant Function"]:
        import_module = __import__(i)
        callable_Data.append(import_module.callable())
    jsondict = json.dumps(callable_Data[0])
    df = pd.read_json(jsondict, orient='columns')
    #print(df)
    tool_condition = df.iloc[-1, 1]
    if tool_condition == "Unworn":
        alarm = "OFF"
    else:
        alarm = "ON"
    record_time = df.iloc[-1, 0]
    reply_json = []
    reply_json.append({"Time": record_time, "tool_condition" : tool_condition, "alarm" : alarm})
    print(reply_json)
    return reply_json
#print(execute())
