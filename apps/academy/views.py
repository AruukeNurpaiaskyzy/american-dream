from django.shortcuts import render
from apps.academy.models import Settings, Contacts

# Create your views here.
def settings(request):
    settings = Settings.objects.latest("id")
    contact = Contacts.objects.latest("id")
    return render (request, 'index.html', locals())