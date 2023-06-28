from django.urls import path,include
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('twininterface/', include('twininterface.urls')),
    path('notifierservice/', include('notifierservice.urls')),

]