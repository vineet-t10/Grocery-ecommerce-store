from unicodedata import name
from django.urls import path
from .views import MainView,search,defaultcarts

urlpatterns = [
    path('',MainView,name='main-page'),
    path('search/',search,name="search-page"),
    
]