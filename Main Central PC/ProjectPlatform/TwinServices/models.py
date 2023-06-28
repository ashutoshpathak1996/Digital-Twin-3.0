from django.db import models
from account.models import Account
from twinregister.models import VerticleMilling

# Create your models here.

class Services_Outsourced(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'
        

class serviceproviders(models.Model):
    

    serviceprovider = models.ForeignKey(Account, limit_choices_to= {'is_serviceprovider' : True},on_delete=models.CASCADE, null=True) 
    


    def __str__(self):
        return f'{self.serviceprovider}'

class NotificationService(models.Model):

    manufacturer = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='mfg') 
    serviceprovider = models.ForeignKey(serviceproviders, on_delete=models.SET_NULL, null=True,related_name='sp') 
    twin_selected = models.ForeignKey(VerticleMilling,on_delete=models.SET_NULL, null=True) 
    services = models.ManyToManyField(Services_Outsourced)


    def __str__(self):
        return f'{self.serviceprovider}'

