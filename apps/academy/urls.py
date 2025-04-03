from django.urls import path

from apps.academy.views import settings, AboutView, courses

urlpatterns = [
    path('', settings, name="settings"),
    path("about/", AboutView.as_view(), name='about'),
    path("courses/", courses, name='courses')
    



]
