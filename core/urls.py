from django.urls import path
from .views import Home, CreateCar, Auction

urlpatterns = [
    path("", Home.as_view(), name="home_page"),
    path("create/", CreateCar.as_view(), name="create"),
    path("auction/<int:pk>/", Auction.as_view(), name="auction"),
]
