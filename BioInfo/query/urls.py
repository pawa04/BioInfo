from django.contrib import admin
from django.urls import path
from query import views 


urlpatterns = [ path("",views.welcome)
   
    # Define other URL patterns as needed
]