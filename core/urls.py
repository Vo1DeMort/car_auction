from django.urls import path
from .views import Home, CreateCar, Auction, profile, UpdateCar, DeleteCar

urlpatterns = [
    path("", Home.as_view(), name="home_page"),

    path("create/", CreateCar.as_view(), name="create"),
    path("update/<int:pk>/", UpdateCar.as_view(), name="update_car"),
    path("delete/<int:pk>/", DeleteCar.as_view(), name="delete_car"),

    path("auction/<int:pk>/", Auction.as_view(), name="auction"),
    path("profile/", profile, name="profile"),
]
