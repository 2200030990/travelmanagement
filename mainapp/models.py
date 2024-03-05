from django.db import models

# Create your models here.
class Register(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    class Meta:
        db_table="Register"

class Topplaces(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=3000)
    photo = models.ImageField(upload_to = 'static/img')
    TimetoVisit = models.CharField(max_length=250)
    HowtoReach = models.CharField(max_length=250)
    Attractions = models.CharField(max_length=1000)
    class Meta:
        db_table = "Topplaces"

class Tophotels(models.Model):
    hotelname = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='static/img/hotels')
    description = models.CharField(max_length=3000)
    highlights = models.CharField(max_length=1000)

    class Meta:
        db_table = "Tophotels"
