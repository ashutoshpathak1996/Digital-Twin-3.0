import pandas as pd
import json
import pickle
import os


parent_dir = os.getcwd()
def introduction():
    function_type = 'AnalyticFunction'
    dependant_functions = []
    active_passive = 'Active'
    performative_types = ['request_analytic']
    return {'Function Type':function_type,'Dependant Function':dependant_functions, 'active_passive' : active_passive, "performative_types": performative_types}

def callable():
    with open(parent_dir + r"\Application and Service Agent\DataBase\analytic_tool_condition\tool_condition.json", 'r') as f:
        tool_report = json.load(f)
    return tool_report

def make_predictions(df, model_filepath):
    # Wrangle JSON file
    X_test = df
    # Load model
    with open(model_filepath, "rb") as f:
        model = pickle.load(f)
    # Generate predictions
    y_test_pred = model.predict(X_test)
    # Put predictions into Series , and same index as X_test
    y_test_pred = pd.Series(y_test_pred, index=X_test.index, name="tool_condition")
    return y_test_pred

def Active():
    print("Tool Monitoring Started")
    import datetime
    import time
    reply_json = []
    while True:
        df_random=pd.read_csv(parent_dir + r"\Machine_Twin 1\MachineCommunication\Test_DataSets.csv")
        df_random1 = df_random.sample(n=1)
        # Generate predictions
        y_test_pred = make_predictions(
            df_random1,
            model_filepath=parent_dir + r"\Application and Service Agent\MachineLearningModels\model_ensemle_bagging_rf_binary_classi.pkl",
        )
        value=y_test_pred.iloc[0]
        if value==1:
            p="Worn"
        else:
            p="Unworn"
        if p=="Worn":
            print("Change Tool")
            record_time = (datetime.datetime.now()).strftime("%d-%m-%Y %H:%M:%S:%f")
            reply_json.append({"Time":record_time, "Tool_Condition": p})
            print(reply_json)
            with open(parent_dir + r"\Application and Service Agent\DataBase\analytic_tool_condition\tool_condition.json", 'w+') as f:
                f.write(json.dumps(reply_json))
                f.close()
            break
        else:
            record_time = (datetime.datetime.now()).strftime("%d-%m-%Y %H:%M:%S:%f")
            reply_json.append({"Time":record_time, "Tool_Condition": p})
            print(reply_json)
            with open(parent_dir + r"\Application and Service Agent\DataBase\analytic_tool_condition\tool_condition.json", 'w+') as f:
                f.write(json.dumps(reply_json))
                f.close()
        time.sleep(15)
#Active()
#x=callable()
#print(x)
