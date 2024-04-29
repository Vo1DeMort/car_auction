from django.contrib import admin
from .models import AppUser, Car, Bid

admin.site.register(AppUser)
admin.site.register(Car)
admin.site.register(Bid)
