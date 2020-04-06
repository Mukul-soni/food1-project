from django.db import models
from django.urls import  reverse
from django.contrib.auth.models import User

# Create your models here.
class Itm(models.Model):
    def __str__(self):
        return self.Itm_name


    Itm_name=models.CharField(max_length=200)
    Itm_dec=models.CharField(max_length=200)
    Itm_price=models.IntegerField()
    Itm_image=models.CharField(max_length=500, default="https://assets.bonappetit.com/photos/5c62e4a3e81bbf522a9579ce/master/pass/milk-bread.jpg")
    
    
    def get_absolute_url(self):
        return reverse("food1:detail", kwargs={"pk":self.pk})