import random
import pandas as pd
import scipy.stats as stats
import numpy as np
import json
import sys
import os


parent_dir = os.getcwd()
def introduction():
    function_type = 'RecommendationGeneration'
    dependant_functions = ['analytic_machine_condition', 'analytic_tool_condition']
    active_passive = 'Passive'
    performative_types = 'request_recommendation'
    return {'Function Type':function_type,'Dependant Function':dependant_functions, 'active_passive' : active_passive, "performative_types": performative_types}

def execute():
    return recommendation_generation()

def recommendation_generation():
    sys.path.append(parent_dir + r"\Application and Service Agent\DownloadableFunctions")
    #sys.path.append("C:\\Users\\ashut\\OneDrive\\Desktop\\Final Deployment\\Physical Assets\\HMI_1\\Application and Service Agent\\DownloadableFunctions")
    x = introduction()
    #print(x["Dependant Function"])
    callable_Data=[]
    for i in x["Dependant Function"]:
        import_module = __import__(i)
        callable_Data.append(import_module.callable())
    jsondict = json.dumps(callable_Data[0])
    df = pd.read_json(jsondict, orient='columns')
    #print(df)
    critical = int(len(df)*0.1)*-1
    avg_temp = df.iloc[critical:, 2]
    temp = round(sum(avg_temp)/len(avg_temp),2)
    if temp>=450:
        recommend_coolant = "YES"
    else:
        recommend_coolant = "NO"
    record_time_machine = df.iloc[-1, 0]
    jsondict_t = json.dumps(callable_Data[1])
    df_t = pd.read_json(jsondict_t, orient='columns')
    tool_condition = df_t.iloc[-1, 1]
    record_time_tool = df_t.iloc[-1, 0]
    if tool_condition=="Worn":
        tool_change = "YES"
    else:
        tool_change = "NO"
    reply_json = []
    reply_json.append({"Time_m": record_time_machine, "avg_temp" : str(temp), "recommend_coolant" : recommend_coolant, "Time_t": record_time_tool, "tool_change": tool_change})
    print(reply_json)
    return reply_json
#print(execute())
