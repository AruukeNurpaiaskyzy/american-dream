from django.contrib import admin
from apps.academy.models import Settings, Contacts

# Register your models here.
admin.site.register(Settings)
admin.site.register(Contacts)