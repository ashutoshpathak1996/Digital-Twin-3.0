from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from twinregister.models import VerticleMilling
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from time import time
import json 
from random import random



# Create your views here.
@login_required
def maininterface(request):
    registered_models = VerticleMilling.objects.filter(user=request.user)
    registered_models_connected = registered_models.filter(is_connected=True)
    context = {
        'registered_models_connected' : registered_models_connected,
    }
    return render(request, 'twininterface\maininterface.html',context)

@csrf_exempt
def livecontentbox(request,id):
    print('hel')
    registered_models = VerticleMilling.objects.filter(user=request.user)
    registered_models_connected = registered_models.filter(is_connected=True)
    global selected_model
    mymodel = VerticleMilling.objects.get(pk=id)
    mymodel.refresh_from_db()
    selected_model = mymodel
    global spindlespeed, feed_rate
    spindlespeed = selected_model.spindle_speed
    feed_rate = selected_model.feed_x
    context = {
        'selected_model': selected_model,
        'registered_models_connected' : registered_models_connected,
    }
    return render(request, 'twininterface\livecontentbox.html',context)

@csrf_exempt
def chartdata(request):
    data = {
        "spindle_rpm":[time() * 1000, int(spindlespeed)],
        "feed_rate":[time() * 1000, float(feed_rate)]
    }
    #data = json.dumps(data)
    return HttpResponse(json.dumps(data), content_type="application/json")

