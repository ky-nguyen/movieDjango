from random import choices
from sre_constants import CATEGORY
from unicodedata import category

from django.db import models

# Create your models here.


CATEGORY_CHOICES = (
    ('A', 'ACTIONS'),
    ('D', 'DRAMA'),
    ('C', 'COMEDY'),
    ('R', 'ROMANCE'),
)

LANGUAGE_CHOICES = (
    ('EN', 'ENGLISH'),
    ('VN', 'VIETNAMESE'),
)

STATUS_CHOICES = (
    ('R', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)


    def __str__(self):
        return self.title

