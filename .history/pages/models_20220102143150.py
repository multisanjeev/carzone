from django.db import models

class Teams(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%a/")
    facebook_link = models.URLField()
