from django.db import models
from django.utils.translation import ugettext_lazy as _


class Items(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    upc = models.CharField(max_length=128)
    in_hand = models.IntegerField()