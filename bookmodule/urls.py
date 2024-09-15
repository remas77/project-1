from django.urls import path
from . import views

urlpatterns=[
    path('book/',views.index2,name='index2')
]