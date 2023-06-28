from django import forms
from .models import VerticleMilling


class VerticleMillingForm(forms.ModelForm):
    class Meta:
        model = VerticleMilling
        fields = ['twin_id','display_name','ip_address','port_number','floor_id','tool_aas','spindle_aas','coolant_aas','maxtravel_X','maxtravel_Y','maxtravel_Z','description','otherdetails_link']