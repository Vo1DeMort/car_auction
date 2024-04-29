from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


""" should override id fields to uuid 
    be back when i am done with the functionalities
"""


class AppUser(AbstractUser):
    profile_img = models.ImageField(null=True, blank=True, upload_to="profile_imgs/")
    about_me = models.TextField(null=True, blank=True, max_length=300)

    def __str__(self):
        return self.username


class Car(models.Model):
    # this choices technique was different in django 4
    TRANSMISSIONS = {
        "auto": "auto transmission",
        "manual": "manual transmission",
        "cvt": "continuous variable transmission CVT ",
    }
    DRIVETRAINS = {
        "awd": "all wheel drive",
        "fwd": "front-wheel drive",
        "rwd": "rear-wheel drive",
        "4wd": "four-wheel drive",
    }
    owner = models.ForeignKey(
        # AppUser,
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="car_owner",
        null=True,
        blank=True,
    )
    car_model = models.CharField(max_length=20)
    car_company = models.CharField(max_length=20)
    year = models.DateField(help_text="the year in which the car was made")
    made_in = models.CharField(max_length=10, help_text="made in which country")
    milage = models.FloatField()
    transmission_type = models.CharField(max_length=6, choices=TRANSMISSIONS)
    drivetrain = models.CharField(max_length=3, choices=DRIVETRAINS)
    color = models.CharField(max_length=20, null=True, blank=True)
    auction_start_time = models.DateTimeField(auto_now_add=True)
    # this field will be update when available_for_auction is updated
    auction_end_date = models.DateTimeField(auto_now=True)
    available_for_auction = models.BooleanField(default=False)
    # contstains are null just for the developemnt purposes
    images = models.ImageField(upload_to="cars/", null=True, blank=True)
    # need to read about file fields

    class Meta:
        ordering = ["-auction_start_time"]

    def __str__(self):
        return f"{self.car_model} "

    # def get_absolute_url


class Bid(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    # a car can have many bidders
    bidder = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)
    offer = models.DecimalField(max_digits=10, decimal_places=2)
    # a user can make better offers until the auction is done
    offer_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.car.car_model} was offered {self.offer} by {self.bidder.username}"
        )
