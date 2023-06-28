from django import forms
from .models import NotificationService
from account.models import Account
from twinregister.models import VerticleMilling
from .models import Services_Outsourced,serviceproviders


class NotificationServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        users = kwargs.pop('users',None)
        
        super(NotificationServiceForm, self).__init__(*args, **kwargs)
        self.fields['twin_selected'].queryset = VerticleMilling.objects.filter(user = users)
        
    serviceprovider = forms.ModelChoiceField(queryset = serviceproviders.objects.all())
    services = forms.ModelMultipleChoiceField(queryset = Services_Outsourced.objects.all(),widget=forms.CheckboxSelectMultiple)
    twin_selected = forms.ModelChoiceField(queryset = None )
    class Meta:
        model = NotificationService
        fields = ['serviceprovider','twin_selected','services']
    
    