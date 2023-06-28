from django.urls import path,include
from . import views


urlpatterns = [
    path('serviceproviderinterface/', views.serviceproviderinterface, name='serviceproviderinterface'),
    path('mytask/', views.mytask, name='mytask'),
    path('downloaddata/', views.downloaddata, name='downloaddata'),
     

]