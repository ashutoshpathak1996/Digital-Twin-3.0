import json
import sys
import csv
import pandas as pd
import datetime


def introduction():
    function_type = 'OrderManager'
    dependant_functions = []
    active_passive = 'Passive'
    performative_types = 'request_orderstatus'
    return {'Function Type':function_type,'Dependant Function':dependant_functions, 'active_passive' : active_passive, "performative_types": performative_types}

def execute():
    return order_alldetails()

def order_alldetails():
    filepath = "C:\\Users\\ashut\\OneDrive\\Desktop\\Custom Function Integration\\Operation and Management Agent\\DataBase\\orderStatus\\orderstatus.xlsx"
    fileraw_val = pd.read_excel(filepath)
    reply_json = []
    for index, row in fileraw_val.iterrows():
        reply_json.append({
            "job_id" : row["job_id"],
            "due_date": str(row["job_due_date"].to_pydatetime().date()),
            "route" : row["job_route"],
            "current_location": row["current_location"]
        })
    return reply_json
#print(execute())
