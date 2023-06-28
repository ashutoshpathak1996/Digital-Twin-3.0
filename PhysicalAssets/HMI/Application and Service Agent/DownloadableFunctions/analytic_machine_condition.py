import random
import pandas as pd
import scipy.stats as stats
import numpy as np
import json
import os
import csv

parent_dir = os.getcwd()
def introduction():
    function_type = 'AnalyticFunction'
    dependant_functions = []
    active_passive = 'Active'
    performative_types = ['request_analytic']
    return {'Function Type':function_type,'Dependant Function':dependant_functions, 'active_passive' : active_passive, "performative_types": performative_types}

def callable():
    with open(parent_dir + r"\Application and Service Agent\DataBase\analytic_machine_condition\machine_condition.json", 'r') as f:
        machine_report = json.load(f)
    return machine_report

def Active():
    print('Machine Monitoring Started')
    import datetime
    import time
    reply_json = []
    while True:
        df = pd.read_csv(parent_dir + r"\Machine_Twin 1\MachineCommunication\my_data.csv")
        df_vibration = df[['vibration_x', 'vibration_y', 'vibration_z']]
        #Splitting Data into 80:20 ratio
        cutt_off = int(len(df_vibration)*0.8)
        df_historical = df_vibration.iloc[:cutt_off]
        df_recent = df_vibration.iloc[cutt_off:]
        critical_amplitude_factor = 2.5
        df_historical.loc[:, 'vibration_x'] = df['vibration_x'] * critical_amplitude_factor
        # Hypothesis Testting for X-axis vibration, i.e to test whether mean vibrations of recent x-axis are double that of hostorical
        data_group1 = np.array(df_historical['vibration_x'])
        data_group2 = np.array(df_recent['vibration_x'])
        # Perform the two sample t-test
        p_value = round(stats.ttest_ind(a=data_group1, b=data_group2, equal_var=True, alternative='greater')[1],4)
        # Temperature reading from Machine Communication Folder
        with open(parent_dir + r"\Machine_Twin 1\MachineCommunication\Temperature_Sensor.csv", 'r') as file:
          csvreader = csv.reader(file)
          for row in csvreader:
              temp=row[0]
        record_time = (datetime.datetime.now()).strftime("%d-%m-%Y %H:%M:%S:%f")
        reply_json.append({"Time": record_time, "p_value" : str(p_value), "temp" : str(temp)})
        print(reply_json)
        with open(parent_dir + r"\Application and Service Agent\DataBase\analytic_machine_condition\machine_condition.json", 'w+') as f:
            f.write(json.dumps(reply_json))
            f.close()
        time.sleep(15)
