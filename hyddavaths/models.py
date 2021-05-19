from django.db import models

# Create your models here.
class scroler(models.Model):
    # title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='scrolers')
class gallery_photo(models.Model):
    image = models.ImageField(upload_to='gallery')
