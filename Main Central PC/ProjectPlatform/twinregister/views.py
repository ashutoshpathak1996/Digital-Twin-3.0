from django.shortcuts import render,redirect
from .forms import VerticleMillingForm
from account.models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import socket
from FIPAsupport.messaging import *
from .models import VerticleMilling
import threading
import time
# Create your views here.
import requests



@login_required
def twinregisteration(request):
    if request.user.is_manufacturer == False:
        return HttpResponseNotFound("Login with manufacturer id")
    if request.method == 'POST':
        form = VerticleMillingForm(request.POST)
        fields = ['twin_id','display_name','ip_address','port_number','floor_id','tool_aas','spindle_aas','coolant_aas','maxtravel_X','maxtravel_Y','maxtravel_Z','description','otherdetails_link']
        if form.is_valid():
            twin_template = VerticleMilling()
            twin_template.user = request.user
            twin_template.twin_id = form.cleaned_data['twin_id']
            twin_template.display_name = form.cleaned_data['display_name']
            twin_template.ip_address = form.cleaned_data['ip_address']
            twin_template.port_number = form.cleaned_data['port_number']
            twin_template.floor_id = form.cleaned_data['floor_id']
            twin_template.tool_aas = form.cleaned_data['tool_aas']
            twin_template.spindle_aas = form.cleaned_data['spindle_aas']
            twin_template.coolant_aas = form.cleaned_data['coolant_aas']
            twin_template.maxtravel_X = form.cleaned_data['maxtravel_X']
            twin_template.maxtravel_Y = form.cleaned_data['maxtravel_Y']
            twin_template.maxtravel_Z = form.cleaned_data['maxtravel_Z']
            twin_template.description = form.cleaned_data['description']
            twin_template.otherdetails_link = form.cleaned_data['otherdetails_link']
            twin_template.save()
            messages.success(request, "Registration successful")
            return redirect('/account/twininterface/twinregister/twinregisteration/')

    
    return render(request, 'twinregister/twinregisteration.html')

def verticalcncmilling(request):
    form = VerticleMillingForm(request.POST)

    context = {
        'form': form,
    }
    
    return render(request, 'twinregister/verticlecncmilling.html',context)

#For javascript function of button ping twin
@csrf_exempt
def pingtwin(request):
    ## Getting the data from frontend
    platform_id = 1234 ## Manual identifier

    twin_id = request.GET.get("twin_id",None)
    ip_address = request.GET.get("ip_address",None)
    port_number = request.GET.get("port_number",None)
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = 'query_meta_data'
    msg1.content = 'platform_registration'


    ##Socket creation

    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)


    ## sending the agent_id of platform to server
    while True:
        # try:
        message = client.recv(1024)
        if len(message) > 0:
            msg = message
            while len(message) >1023:
                message = client.recv(1024)
                msg+=message

            msg = unflatten(message)
            # if the server send a NICK then
            # we send the platform_id back
            if msg.protocol == "DUMMY_FIPA":
                if msg.type == "server_topics" and msg.content == 'NICK':
                    client.send(flatten(dummyFIPA("server_topics", platform_id)))
            if msg.type == 'agreed':
                data = json.loads(msg.content)
                
                break
            else:

                message = flatten(msg1)
                client.send(message)
            






    # data, addr = s.recvfrom(1024)
    # data = data.decode('utf-8')

    # data = json.loads(data)
    # s.close()

    
    return JsonResponse({'data': data})
    


    ### For connection
@login_required
def twinconnection(request):
    registered_models = VerticleMilling.objects.filter(user=request.user)
    registered_models_connected = registered_models.filter(is_connected=True)
    registered_models_disconnected = registered_models.filter(is_connected=False)

    context = {
        'registered_models': registered_models,
        'registered_models_connected' : registered_models_connected,
        'registered_models_disconnected' : registered_models_disconnected
    }
    return render(request, 'twinregister/twinconnection.html',context)

@csrf_exempt
def connectionReqTwin(request):
    model_id = request.POST.get("model_id",None)
    selected_model = VerticleMilling.objects.get(pk=model_id)

    platform_id = 1234 ## Manual identifier
    platform_modelid = platform_id + int(model_id)

    twin_id = selected_model.twin_id
    ip_address = selected_model.ip_address
    port_number = selected_model.port_number
    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)


    def connect_to_twin_server(client):



        ## Preparing a FIPA message
        msg1 = FIPA_message()
        msg1.protocol = 'query_interaction_protocol'
        msg1.performative = 'query_ref'
        msg1.sender = platform_modelid
        msg1.receiver = twin_id
        msg1.type = 'query_meta_data'
        msg1.content = 'platform_connection'

        ## sending the agent_id of platform to server
        count = 1
        while True:
            
            try:
                message = client.recv(1024)
                
                
                if len(message) > 0:
                    msg = message
                    while len(message) >1023:
                        message = client.recv(1024)
                        msg+=message

                    msg = unflatten(message)
                    # if the server send a NICK then
                    # we send the platform_id back
                    if msg.protocol == "DUMMY_FIPA" and count == 1:
                        count += 1
                        if msg.type == "server_topics" and msg.content == 'NICK':
                            client.send(flatten(dummyFIPA("server_topics", platform_modelid)))
                    if msg.type == 'agreed':
                        #print('connect')
                        data = json.loads(msg.content)
                        fields = ['floor_id','tool_aas','spindle_aas','coolant_aas','maxtravel_X','maxtravel_Y','maxtravel_Z','programfile_link','otherdetails_link','emergency_on','coolant_on','spindle_on','cycle_on','wcsoffset_X','wcsoffset_Y','wcsoffset_Z','axis_pos_x','axis_pos_y','axis_pos_z','feed_x','feed_y','feed_z','job_file_name','spindle_speed']
                        selected_model.emergency_on = data.get('emergency_on')
                        selected_model.coolant_on = data.get('coolant_on')
                        selected_model.spindle_on = data.get('spindle_on')
                        selected_model.cycle_on = data.get('cycle_on')
                        selected_model.wcsoffset_X = data.get('wcsoffset_X')
                        selected_model.wcsoffset_Y = data.get('wcsoffset_Y')
                        selected_model.wcsoffset_Z = data.get('wcsoffset_Z')
                        selected_model.axis_pos_x = data.get('axis_pos_x')
                        selected_model.axis_pos_y = data.get('axis_pos_y')
                        selected_model.axis_pos_z = data.get('axis_pos_z')
                        selected_model.feed_x = data.get('feed_x')
                        selected_model.feed_y = data.get('feed_y')
                        selected_model.feed_z = data.get('feed_z')
                        selected_model.job_file_name = data.get('job_file_name')
                        selected_model.spindle_speed = data.get('spindle_speed')
                        
                        # for i in fields:
                        #     setattr(selected_model, i, data.get(i))
                            
                        #     selected_model.save()
                        selected_model.is_connected = True 
                        selected_model.save(update_fields=['emergency_on','coolant_on','spindle_on','cycle_on','wcsoffset_X','wcsoffset_Y','wcsoffset_Z','axis_pos_x','axis_pos_y','axis_pos_z','feed_x','feed_y','feed_z','job_file_name','spindle_speed','is_connected'])
                        #messages.success(request, "connection successful")
                        
                        

                    else:
                        if count ==2:
                            message = flatten(msg1)
                            client.send(message)
                            count+=1
            except:
                continue
        return
    thread = threading.Thread(target=connect_to_twin_server, args=(client,))
    thread.start()           
    time.sleep(2)
    #thread.join()
    if selected_model.is_connected == True:
        messages.success(request, "connection successful")
        return JsonResponse({"status":"success"})
    else:
        #messages.error(request, "connection failed")
        return JsonResponse({"status":"failed"})


## Disconnection functions
@csrf_exempt
def disconnectionReqTwin(request):
    model_id = request.POST.get("model_id",None)
    selected_model = VerticleMilling.objects.get(pk=model_id)

    platform_id = 1234 ## Manual identifier
    platform_modelid = platform_id + int(model_id)

    twin_id = selected_model.twin_id
    ip_address = selected_model.ip_address
    port_number = selected_model.port_number
    agent_server = (ip_address, int(port_number))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(agent_server)
    def disconnect_to_twin_server():

        ## Preparing a FIPA message
        msg1 = FIPA_message()
        msg1.protocol = 'query_interaction_protocol'
        msg1.performative = 'query_ref'
        msg1.sender = platform_modelid
        msg1.receiver = twin_id
        msg1.type = 'query_meta_data'
        msg1.content = 'platform_disconnection'
        
        while True:
            # try:
            message = client.recv(1024)
            
            
            if len(message) > 0:
                msg = message
                while len(message) >1023:
                    message = client.recv(1024)
                    msg+=message

                msg = unflatten(message)
                # if the server send a NICK then
                # we send the platform_id back
                if msg.protocol == "DUMMY_FIPA":
                    if msg.type == "server_topics" and msg.content == 'NICK':
                        client.send(flatten(dummyFIPA("server_topics", platform_modelid)))
                else:
                    message = flatten(msg1)
                    client.send(message)
                    selected_model.is_connected = False
                    selected_model.save()
                    break
            message = flatten(msg1)
            client.send(message)
            selected_model.is_connected = False
            selected_model.save()
            break
        return 
    disconnect_to_twin_server()

    if selected_model.is_connected == False:
        messages.success(request, "Disconnected ")
        return JsonResponse({"status":"success"})
    else:
        messages.error(request, "disconnection failed")
        return JsonResponse({"status":"failed"})


def twindisplaydata(request):
    registered_models = VerticleMilling.objects.filter(user=request.user)
    registered_models_connected = registered_models.filter(is_connected=True)
    

    context = {
        'registered_models': registered_models,
        'registered_models_connected' : registered_models_connected,
        
    }
    return render(request, 'twinregister/twindisplaydata.html',context)
    


   
def displaydatabox(request, pk):
    registered_models = VerticleMilling.objects.filter(user=request.user)
    registered_models_connected = registered_models.filter(is_connected=True)
    mymodel = VerticleMilling.objects.get(pk=pk)
    mymodel.refresh_from_db()
    selected_model = mymodel

    ## For vertilce mill model
    tool_url = selected_model.tool_aas
    spindle_url = selected_model.spindle_aas
    coolant_url = selected_model.coolant_aas

    tr = requests.get(tool_url)
    sr = requests.get(spindle_url)
    cr = requests.get(coolant_url)

    tool_data = tr.json()
    spindle_data = sr.json()
    coolant_data = cr.json()

    
    
    context = {
        
        'selected_model': selected_model,
        'registered_models': registered_models,
        'registered_models_connected' : registered_models_connected,
        'tool_data' : tool_data,
        'spindle_data' : spindle_data,
        'coolant_data' : coolant_data,
        
    }
 
    return render(request, 'twinregister/displaydatabox.html',context)



def connectbox(request,pk):
    registered_models = VerticleMilling.objects.filter(user=request.user)
    selected_model = VerticleMilling.objects.filter(pk=pk).values()[0]
    
    context = {
        
        'selected_model': selected_model,
        'registered_models': registered_models,
        
    }
    return render(request, 'twinregister/connectbox.html',context)


### getting data and esctablishing continuous connection with server

# @csrf_exempt
# def connecttwinbtn(request):
#     ## Getting the data from frontend
#     def disconnect(client):
        

#         ## Preparing a FIPA message
#         msg1 = FIPA_message()
#         msg1.protocol = 'query_interaction_protocol'
#         msg1.performative = 'query_ref'
#         msg1.sender = platform_modelid
#         msg1.receiver = twin_id
#         msg1.type = 'query_meta_data'
#         msg1.content = 'platform_disconnection'
        
#         while True:
#             # try:
#             message = client.recv(1024)
            
            
#             if len(message) > 0:
#                 msg = message
#                 while len(message) >1023:
#                     message = client.recv(1024)
#                     msg+=message

#                 msg = unflatten(message)
#                 # if the server send a NICK then
#                 # we send the platform_id back
#                 if msg.protocol == "DUMMY_FIPA":
#                     if msg.type == "server_topics" and msg.content == 'NICK':
#                         client.send(flatten(dummyFIPA("server_topics", platform_modelid)))
#                 else:
#                     message = flatten(msg1)
#                     client.send(message)
#                     selected_model.is_connected = False
#                     selected_model.save()
#                     break




        
#     model_id = request.GET.get("model_id",None)
#     platform_id = 1234 ## Manual identifier
#     platform_modelid = platform_id + int(model_id)

#     twin_id = request.GET.get("twin_id",None)
#     #model_id = request.GET.get("model_id",None)
#     ip_address = request.GET.get("ip_address",None)
#     port_number = request.GET.get("port_number",None)
#     global client
#     agent_server = (ip_address, int(port_number))
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect(agent_server)

#     selected_model = VerticleMilling.objects.get(pk=model_id)
#     if selected_model.is_connected == True:
#         thread = threading.Thread(target=disconnect, args=(client,))
#         thread.start()

#     else:

        
        

#         ## Preparing a FIPA message
#         msg1 = FIPA_message()
#         msg1.protocol = 'query_interaction_protocol'
#         msg1.performative = 'query_ref'
#         msg1.sender = platform_modelid
#         msg1.receiver = twin_id
#         msg1.type = 'query_meta_data'
#         msg1.content = 'platform_connection'


#         ##Socket creation

        

        
#         ## sending the agent_id of platform to server
#         while True:
#             # try:
#             message = client.recv(1024)
            
            
#             if len(message) > 0:
#                 msg = message
#                 while len(message) >1023:
#                     message = client.recv(1024)
#                     msg+=message

#                 msg = unflatten(message)
#                 # if the server send a NICK then
#                 # we send the platform_id back
#                 if msg.protocol == "DUMMY_FIPA":
#                     if msg.type == "server_topics" and msg.content == 'NICK':
#                         client.send(flatten(dummyFIPA("server_topics", platform_modelid)))
#                 if msg.type == 'agreed':
#                     data = json.loads(msg.content)
#                     fields = ['floor_id','tool_aas','spindle_aas','coolant_aas','maxtravel_X','maxtravel_Y','maxtravel_Z','programfile_link','otherdetails_link','emergency_on','power_on','is_loaded','cycle_on','wcsoffset_X','wcsoffset_Y','wcsoffset_Z']
#                     for i in fields:
#                         setattr(selected_model, i, data.get(i))
                        
#                         selected_model.save()
#                     selected_model.is_connected = True 
#                     selected_model.save()
                    

#                 else:

#                     message = flatten(msg1)
#                     client.send(message)
                






#         # data, addr = s.recvfrom(1024)
#         # data = data.decode('utf-8')

#         # data = json.loads(data)
#         # s.close()

    
#     return JsonResponse({'data': 'done'})      
        
