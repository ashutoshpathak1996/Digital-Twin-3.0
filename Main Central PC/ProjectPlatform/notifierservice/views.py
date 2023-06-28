from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from TwinServices.models import NotificationService,serviceproviders
from FIPAsupport.messaging import *
import socket
import pandas as pd
from django.http import HttpResponse
# Create your views here.
ip_address = "10.96.37.254"
@login_required
def serviceproviderinterface(request):
    return render(request, 'notifierservice\spinterface.html')

@login_required
def mytask(request):
    su = serviceproviders.objects.get(serviceprovider =request.user)
    tasks = NotificationService.objects.filter(serviceprovider=su)
    context = {'tasks': tasks}
    return render(request, 'notifierservice\mytask.html',context)
@csrf_exempt
def downloaddata(request):
    platform_id = 12341 ## Manual identifier
    model_id = request.POST.get("model_id",None)
    print(model_id)
    model_fetch = NotificationService.objects.get(pk = model_id)
    twin_selected_id = str(model_fetch.twin_selected.twin_id)
    service_type = str(request.POST.get("ser_type",None))
    print(twin_selected_id,service_type,type(service_type))


    twin_id = 111111009
    #ip_address = '10.96.25.239'
    port_number = 80
    ## Preparing a FIPA message
    msg1 = FIPA_message()
    msg1.protocol = 'query_interaction_protocol'
    msg1.performative = 'query_ref'
    msg1.sender = platform_id
    msg1.receiver = twin_id
    msg1.type = service_type
    msg1.content = twin_selected_id


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
                if msg.type == 'inform_sp_req':
                    
                    data = json.loads(msg.content)
                    df_json = pd.read_json(msg.content)
                    df_excel = df_json.to_excel('media/13.xlsx')
                    
                                    
                    return HttpResponse('hello')
                    
                
                else:
                    #print('j')
                    if count ==2:
                            message = flatten(msg1)
                            client.send(message)
                            count+=1
        except:
            break