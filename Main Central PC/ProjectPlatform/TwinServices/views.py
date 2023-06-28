from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.core.files.storage import FileSystemStorage
from twinregister.models import VerticleMilling
from FIPAsupport.messaging import *
import socket
from platformfunctions.CostFunction import * 
from platformfunctions.toolPathOptimization_Google_firstSolutionStrategy import * 
from .forms import NotificationServiceForm
from .models import NotificationService,Services_Outsourced
from django.contrib import messages, auth
from django.views.decorators.csrf import csrf_exempt
import os

global ip_address, port_number
with open(r'../server_ip.txt') as f:
    lines=[]
    for line in f.readlines():
        lines.append(line)
    port_number = int(lines[0])
    ip_address = lines[1]
    f.close()
#ip_address = 'localhost'
# Create your views here.
def tpgCE(request):
    
    if request.method == 'POST':
        uploaded_file = request.FILES['stpfile']
        #print(uploaded_file.name)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        pathname = '.'+fs.url(uploaded_file.name)
        textfile,holesNo,distance,feed = toolPathOptimization(pathname)
       
        response = HttpResponse(content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename = code.gcd'
        response.writelines(textfile)
        
        
        return response

    
    return render(request, 'TwinServices/tpgCE.html')

def costeval(request):
    
    if request.method == 'POST':
        uploaded_file = request.FILES['stpfile']
        #print(uploaded_file.name)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        pathname = '.'+fs.url(uploaded_file.name)
        textfile,holesNo,distance,feed = toolPathOptimization(pathname)
        global costfunc
        costfunc = costFunction(distance,holesNo)
        costfunc = int(costfunc)
        context ={
            'cost':costfunc
        }
        return render(request, 'TwinServices/costeval.html',context)

        
        
        
        
        

    
    return render(request, 'TwinServices/costeval.html')


## For queries
def queriesmain(request):
    return render(request, 'TwinServices/queriesmain.html')

## planning-> free machines service
def freemachines(request):
    registered_models = VerticleMilling.objects.filter(user=request.user)
    registered_models_connected = registered_models.filter(is_connected=True)
    registered_models_loaded = registered_models_connected.filter(is_loaded=False)
    context = {'registered_models_loaded': registered_models_loaded}


    return render(request, 'TwinServices/freeMachines.html',context)

## Inventory -> Purchase Requirements
def purchase_requirements(request):
    return render(request, 'TwinServices/purchasereq.html')
def purchase_requirements_conn(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111001
    #ip_address = '10.96.33.70'
    #port_number = 85
    ## Preparing a FIPA message
    print("Current Working Directory",os.getcwd())
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_inventory'
    msg1.content = 'request_purchase_requirement'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA" and count == 1:
                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_purchase_req':
                    #print('h')
                    data = json.loads(msg.content)
                    #print(data)
                    context = {'data' : data}
                    return render(request, 'TwinServices/purchasereqconn.html',context)
                    
                
                else:
                    #print('j')
                    if count ==2:
                            message = flatten(msg1)
                            client.send(message)
                            count+=1
        except:
            break


## Inventory -> raw_materials_details
def raw_materials_details(request):
    return render(request, 'TwinServices/rawmaterialsdetails.html')

def raw_material_floor(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111001
    #ip_address = '10.96.33.70'
    #port_number = 85
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_inventory'
    msg1.content = 'request_rawmaterial_detail_floor'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA" and count == 1:

                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_rawmaterialfloor_req':
                    
                    data = json.loads(msg.content)
                    context = {'data' : data}
                    return render(request, 'TwinServices/rawmaterialfloor.html',context)
                    
                
                else:
                        #print('j')
                        if count ==2:
                                message = flatten(msg1)
                                client.send(message)
                                count+=1
        except:
            break

def raw_material_machine(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111001
    #ip_address = '10.96.33.70'
    #port_number = 85
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_inventory'
    msg1.content = 'request_rawmaterialmachine_detail'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA"and count == 1:
                    
                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_rawmaterialmachine_req':
                    
                    data = json.loads(msg.content)
                    context = {'data' : data}
                    return render(request, 'TwinServices/rawmaterialmachine.html',context)
                    
                
                else:
                        #print('j')
                        if count ==2:
                                message = flatten(msg1)
                                client.send(message)
                                count+=1
        except:
            break


## Inventory -> work in process
def wip_details(request):
    return render(request, 'TwinServices/wipdetails.html')

def wipdetail_conn(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111001
    #ip_address = '10.96.33.70'
    #port_number = 85
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_inventory'
    msg1.content = 'request_wip_details'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA"and count == 1:
                    
                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_wip_req':
                    
                    data = json.loads(msg.content)
                    TotalUnderprocessJob = 0
                    TotalWaitingJob = 0
                    for items in data:
                        TotalUnderprocessJob += len(items["underprocess"])
                        TotalWaitingJob += len(items["waiting"])

                    context = {
                        'data' : data,
                        'TotalWaitingJob' : TotalWaitingJob,
                        'TotalUnderprocessJob':TotalUnderprocessJob

                        }
                    return render(request, 'TwinServices/wipdetailconn.html',context)
                    
                
                else:
                        #print('j')
                        if count ==2:
                                message = flatten(msg1)
                                client.send(message)
                                count+=1
        except:
            break

def finish_goods_details(request):
    return render(request, 'TwinServices/finishedgoods.html')

def finishedgooddetail_conn(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111001
    #ip_address = '10.96.33.70'
    #port_number = 85
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_inventory'
    msg1.content = 'request_finishedgoods_details'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA" and count == 1:
                    
                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_fg_req':
                    
                    data = json.loads(msg.content)
                    
                    context = {
                        'data' : data

                        }
                    return render(request, 'TwinServices/finishedgooddetail_conn.html',context)
                    
                
                else:
                        #print('j')
                        if count ==2:
                                message = flatten(msg1)
                                client.send(message)
                                count+=1
        except:
            break


#OrderStatus - > all details
def order_alldetails(request):
    return render(request, 'TwinServices/orderalldetails.html')

def order_alldetails_conn(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111001
    #ip_address = 'localhost'
    #port_number = 85
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_orderstatus'
    msg1.content = 'request_orderstatus'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                #print(msg.type)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA"and count == 1:
                    
                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_orderdetails_req':
                    
                    data = json.loads(msg.content)
                    context = {
                        'data' : data

                        }
                    return render(request, 'TwinServices/order_alldetails_conn.html',context)
                    
                
                else:
                        #print('j')
                        if count ==2:
                                message = flatten(msg1)
                                client.send(message)
                                count+=1
        except:
            break

#MaintainenceStatus - > Query
def maint_alldetails(request):
    return render(request, 'TwinServices\Querying_maintainence\maintainence.html')

def maint_alldetails_conn(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111001
    #ip_address = '10.96.33.70'
    #port_number = 80
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_orderstatus'
    msg1.content = 'maintdetails_requirement'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA"and count == 1:
                    
                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_maintdetails_req':
                    
                    data = json.loads(msg.content)
                    
                    context = {
                        'data' : data

                        }
                    return render(request, 'TwinServices\Querying_maintainence\maint_conn.html',context)
                    
                
                else:
                        #print('j')
                        if count ==2:
                                message = flatten(msg1)
                                client.send(message)
                                count+=1
        except:
            break
## For Analytics
def analyticsmain(request):
    return render(request, 'TwinServices/analyticsmain.html')

#AnalyticsData - > all details
def machinealldetails(request):
    return render(request, 'TwinServices/machinealldetails.html')

def machine_alldetails_conn(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111004
    #ip_address = 'localhost'
    #port_number = 85
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_machinealldetails'
    msg1.content = 'request_machine_report'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                #print(msg.type)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA"and count == 1:
                    
                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_machinedetails_req':
                    data = json.loads(msg.content)
                    context = {
                        'data' : data
                        }
                    return render(request, 'TwinServices/machine_alldetails_conn.html',context)
                    
                
                else:
                        #print('j')
                        if count ==2:
                                message = flatten(msg1)
                                client.send(message)
                                count+=1
        except:
            break

def toolalldetails(request):
    return render(request, 'TwinServices/toolalldetails.html')

def tool_alldetails_conn(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111004
    #ip_address = 'localhost'
    #port_number = 85
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_toolstatus'
    msg1.content = 'request_tool_report'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                #print(msg.type)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA"and count == 1:
                    
                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_tooldetails_req':
                    
                    data = json.loads(msg.content)
                    print(data)
                    context = {
                        'data' : data
                        }
                    return render(request, 'TwinServices/tool_alldetails_conn.html',context)
                    
                
                else:
                        #print('j')
                        if count ==2:
                                message = flatten(msg1)
                                client.send(message)
                                count+=1
        except:
            break
def alarmsmain(request):
    return render(request, 'TwinServices/alarmsmain.html')

def alarmsmachine(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111004
    #ip_address = 'localhost'
    #port_number = 85
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_machinealarms'
    msg1.content = 'request_machine_alarm'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                #print(msg.type)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA"and count == 1:
                    
                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_machinealarms_req':
                    data = json.loads(msg.content)
                    print(data)
                    context = {
                        'data' : data
                        }
                    return render(request, 'TwinServices/alarmsmachine.html',context)
                    
                
                else:
                        #print('j')
                        if count ==2:
                                message = flatten(msg1)
                                client.send(message)
                                count+=1
        except:
            break

def alarmstool(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111004
    #ip_address = 'localhost'
    #port_number = 85
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_toolalarms'
    msg1.content = 'request_tool_alarm'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                #print(msg.type)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA"and count == 1:
                    
                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_toolalarms_req':
                    data = json.loads(msg.content)
                    print(data)
                    context = {
                        'data' : data
                        }
                    return render(request, 'TwinServices/alarmstool.html',context)
                    
                
                else:
                        #print('j')
                        if count ==2:
                                message = flatten(msg1)
                                client.send(message)
                                count+=1
        except:
            break

def recommendation_service(request):
    return render(request, 'TwinServices/recommendation_service.html')

def recommendation_service_conn(request):
    platform_id = 12341 ## Manual identifier

    twin_id = 111111004
    #ip_address = 'localhost'
    #port_number = 85
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_for_recommendation'
    msg1.content = 'request_recommendation'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)

    count = 1
    ## sending the agent_id of platform to server
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(msg)
                #print(msg.type)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA"and count == 1:
                    
                    count += 1
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_id)))
                if msg.type == 'inform_recommendation_req':
                    data = json.loads(msg.content)
                    print(data)
                    context = {
                        'data' : data
                        }
                    return render(request, 'TwinServices/recommendation_service_conn.html',context)
                    
                
                else:
                        #print('j')
                        if count ==2:
                                message = flatten(msg1)
                                client.send(message)
                                count+=1
        except:
            break

def notifier_service(request):
    return render(request, 'TwinServices/Notifier/notifierservice.html')




def addprovider_notifier(request):
    if request.method == 'POST':
        form = NotificationServiceForm(request.POST,users = request.user)

        if form.is_valid():
            #print('hello')
            serviceprovider = form.cleaned_data['serviceprovider']
            twin_selected = form.cleaned_data['twin_selected']
            services = form.cleaned_data.get('services')
            manufacturer = request.user
            #print('hell')
    
            row_data = NotificationService(manufacturer=manufacturer,serviceprovider=serviceprovider,twin_selected=twin_selected)
            row_data.save()
            row_data.services.add(*services)
            row_data.save()
            messages.success(request, "Now service provider have the access of data")
            return redirect('addprovider_notifier')

           
    else:
        form = NotificationServiceForm(users = request.user)
    
    context = { 
        'form': form,
    }

    return render(request, 'TwinServices/Notifier/addprovider.html',context)

def remove_service(request):
    tasks = NotificationService.objects.filter(manufacturer=request.user)
    context = { 
        'tasks' : tasks,
    }
    return render(request, 'TwinServices/Notifier/removeservice.html',context)
@csrf_exempt
def removedata(request):
    model_id = request.POST.get("model_id",None)
    service = request.POST.get("ser_type",None)
    print(model_id)
    model_fetch = NotificationService.objects.get(pk = model_id)
    serid = Services_Outsourced.objects.get(name = service)
    model_fetch.services.remove(serid.id)
    model_fetch.save()
    
    return HttpResponse('success')

