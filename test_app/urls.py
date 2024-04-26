# Create your views here.
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('add_expense/', views.add_expense, name='add_expense')
]