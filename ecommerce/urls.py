from unicodedata import name
from django.urls import path
from .views import MainView,search,cartpe,gotocart,placed

urlpatterns = [
    path('',MainView,name='main-page'),
    path('search/',search,name="search-page"),
    path('cartings/',gotocart,name="cart"),
    path('placed/',placed,name="order-placed"),
    path('cart/<str:description>/<str:price>/<path:image>/',cartpe,name="carts-page"),
    
]