#Passive
def introduction():
    function_type = 'cost_calculation'
    dependant_functions = ['tool_path_optimizer']
    active_passive = 'passive'
    performative_types = ['request_machining_cost']
    return {'function_type': function_type, 'Dependant Function': dependant_functions, "active_passive": active_passive,
            "performative_types": performative_types}

def costFunction(distance,noofholes,depth=20,costperhour=1000,feed=50):
    machiningtime = ((noofholes*depth) + distance)/feed
    cost = costperhour * machiningtime/60000 
    return cost
