from django.urls import path
from . import views

urlpatterns = [
    path('api/smarthome/', views.smarthome_list),
]