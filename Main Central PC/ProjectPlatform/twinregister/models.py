from django.db import models
from account.models import Account
from django.urls import reverse
# Create your models here.

class VerticleMilling(models.Model):
    #Type is System
    # Tool, spindle, and coolants are component

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True) #PLATFORM SPECIFIC
    twin_id = models.CharField(max_length=15)
    display_name = models.CharField(max_length=20) #PLATFORM SPECIFIC
    ip_address = models.CharField(max_length=20) #PLATFORM SPECIFIC
    port_number = models.IntegerField() #PLATFORM SPECIFIC
    is_connected = models.BooleanField(default=False) #PLATFORM SPECIFIC
    floor_id = models.IntegerField()
    tool_aas = models.URLField()
    spindle_aas = models.URLField()
    coolant_aas = models.URLField()
    emergency_on = models.BooleanField(default=False)
    spindle_on = models.BooleanField(default=False)
    coolant_on = models.BooleanField(default=False)
    cycle_on = models.BooleanField(default=False) ## NC cycle status
    spindle_speed = models.CharField(max_length=20)
    axis_pos_x = models.CharField(max_length=20)
    axis_pos_y = models.CharField(max_length=20)
    axis_pos_z = models.CharField(max_length=20)
    job_file_name = models.CharField(max_length=300)
    feed_x = models.CharField(max_length=20)
    feed_y = models.CharField(max_length=20)
    feed_z = models.CharField(max_length=20)
    maxtravel_X = models.CharField(max_length=20)
    maxtravel_Y = models.CharField(max_length=20)
    maxtravel_Z = models.CharField(max_length=20)
    programfile_link = models.CharField(max_length=200, default='')
    wcsoffset_X = models.CharField(max_length=20)
    wcsoffset_Y = models.CharField(max_length=20)
    wcsoffset_Z = models.CharField(max_length=20)
    description = models.TextField(default='') #PLATFORM SPECIFIC
    otherdetails_link = models.URLField()


    def __str__(self):
        return f'{self.display_name}'

    def get_absolute_url(self):
        return reverse("displaydatabox", args=[str(self.id)])