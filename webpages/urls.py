from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('post/<int:id>', views.post, name="post"),
    path('contact', views.contact, name="contact"),
    path('search', views.search, name="search"),
    path('categorysearch/<str:cat>', views.categorysearch, name="categorysearch"),
]
