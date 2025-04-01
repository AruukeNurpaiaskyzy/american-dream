from django.urls import path

from apps.academy.views import settings

urlpatterns = [
    path('', settings, name="settings"),
]