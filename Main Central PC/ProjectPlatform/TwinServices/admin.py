from django.contrib import admin
from .models import Services_Outsourced,serviceproviders,NotificationService
# Register your models here.
admin.site.register(Services_Outsourced)
admin.site.register(serviceproviders)
admin.site.register(NotificationService)