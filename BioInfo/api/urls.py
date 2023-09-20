from django.contrib import admin
from django.urls import path
from api import views 


urlpatterns=[path("",views.getRoutes,name="routes"),
              path('gda/', views.GeneDiseaseAssociationListView.as_view(), name='gda'),
              path('gda/csv/', views.GeneDiseaseAssociationListViewCsv.as_view(), name='gda-csv')]