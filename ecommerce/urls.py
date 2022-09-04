from unicodedata import name
from django.urls import path
from .views import MainView,search,defaultcarts,carts

urlpatterns = [
    path('',MainView,name='main-page'),
    path('search/',search,name="search-page"),
    path('cart/',carts,name="carts-page"),
    

    
]