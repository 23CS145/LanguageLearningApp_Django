# learning/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # other paths if any
]
