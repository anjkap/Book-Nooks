from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)
    min_age = models.IntegerField()
    genre = models.CharField(max_length=100) 
    location = models.CharField(max_length=255)
    rating = models.FloatField()
    rec = models.BooleanField(null=True)

class Review(models.Model):
    review = models.TextField(max_length=2000)
    rating = models.FloatField(null=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    age = models.IntegerField()
    fav_genres = models.CharField(max_length=100)
    bio = models.TextField() 