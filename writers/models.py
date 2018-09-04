from django.db import models
from django.conf import settings


class WritersProfile(models.Model):
    profile_id = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile',
    on_delete=models.CASCADE)


class Bids(models.Model):
    writer_bids = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='writer_bids')


class Order(models.Model):
    order_id = models.ManyToManyField(settings.AUTH_USER_MODEL)
