from django.urls import path
from . import views

urlpatterns = [
    path('contactme', views.contactme, name="contactme"),
]