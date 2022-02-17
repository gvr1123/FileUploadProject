from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('list/', ResumesList, name='list'),
]
