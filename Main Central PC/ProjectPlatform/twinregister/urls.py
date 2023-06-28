from django.urls import path
from . import views


urlpatterns = [
    path('twinregisteration/', views.twinregisteration, name='twinregisteration'),
    path('twinconnection/', views.twinconnection, name='twinconnection'),
    path('twindisplaydata/', views.twindisplaydata, name='twindisplaydata'),
    path('verticalcncmilling/', views.verticalcncmilling, name='verticalcncmilling'),
    path('pingtwin/', views.pingtwin, name='pingtwin'), ##for button click function
    #path('connecttwinbtn/', views.connecttwinbtn, name='connecttwinbtn'), 
    path('connectionReqTwin/', views.connectionReqTwin, name='connectionReqTwin'), ##for button click connect function
    path('disconnectionReqTwin/', views.disconnectionReqTwin, name='disconnectionReqTwin'), ##for button click disconnect function
    path('twindisplaydata/<int:pk>/', views.displaydatabox, name='displaydatabox'),
  

]