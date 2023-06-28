import random
import pandas as pd
import scipy.stats as stats
import numpy as np
import json
import sys
import os


parent_dir = os.getcwd()
def introduction():
    function_type = 'ReportGeneration'
    dependant_functions = ['analytic_machine_condition']
    active_passive = 'Passive'
    performative_types = 'request_machine_report'
    return {'Function Type':function_type,'Dependant Function':dependant_functions, 'active_passive' : active_passive, "performative_types": performative_types}

def execute():
    return report_generation()

def report_generation():
    sys.path.append(parent_dir + r"\Application and Service Agent\DownloadableFunctions")
    x = introduction()
    print(x["Dependant Function"])
    callable_Data=[]
    for i in x["Dependant Function"]:
        import_module = __import__(i)
        callable_Data.append(import_module.callable())
    return callable_Data[0]
#print(execute())
