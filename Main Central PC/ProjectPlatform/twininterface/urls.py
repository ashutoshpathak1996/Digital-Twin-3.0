from django.urls import path,include
from . import views


urlpatterns = [
    path('maininterface/', views.maininterface, name='maininterface'),
    path('livecontentbox/<int:id>', views.livecontentbox, name='livecontentbox'),    
    path('chartdata', views.chartdata, name='chartdata'),    
    path('twinregister/', include('twinregister.urls')),
    path('twinservices/', include('TwinServices.urls')),

  

]