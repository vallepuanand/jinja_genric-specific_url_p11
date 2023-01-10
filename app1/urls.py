from django.urls import path
from app1.views import *
app_name='mavayya'

urlpatterns=[
    path('mawa/',mawa,name='mawa')
]