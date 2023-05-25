from django.urls import path
from googledata import views
urlpatterns=[
     path('',views.index, name="googledataindex"),
]