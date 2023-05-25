from django.urls import path
from microsoftdata import views

urlpatterns=[
    path('',views.index, name="microsoftdataindex"),
]