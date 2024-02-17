from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    #TODO password?

class Comments(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateTimeField()
    comment = models.CharField(max_length=200)

class AuctionListing(models.Model):
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=60)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comments)


class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()