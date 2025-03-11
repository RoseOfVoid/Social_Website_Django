from django.urls import path
from .views import *


app_name = 'account'

urlpatterns = [
    path('login/', user_login, name='login'),
]
