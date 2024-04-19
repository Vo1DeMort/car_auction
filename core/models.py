from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class AppUser(AbstractUser):

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
    color = models.CharField(max_length=20,null=True,blank=True)
    auction_start_time = models.DateTimeField(auto_now_add=True)
    # this field will be update when available_for_auction is updated
    auction_end_date = models.DateTimeField(auto_now=True)
    available_for_auction = models.BooleanField(default=False)
    # contstains are null just for the developemnt purposes
    images = models.ImageField(null=True, blank=True)

    """ transmission_type , drive train and available_for_auction don't show in the retrieve 
        but works in admin panel
    """


    def __str__(self):
        return f"{self.car_model} "

    class Meta:
        ordering = ["-auction_start_time"]


'''

class Bid(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    # a car can have many bidders
    bidder = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)
    offer = models.DecimalField(max_digits=10, decimal_places=2)
    # a user can make better offers until the auction is done
    offer_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car.car_model} of {self.car.owner.username} was offered {self.offer}$ by {self.bidder.username}"
                    '''

