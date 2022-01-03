from django.db import models

class Teams(models.Model):
    first_name = models.CharFields(max_length=255)
    last_name = models.CharFields(max_length=255)
    designation = models.CharFields(max_length=255)
    photo = models..ImageFields(upload_to="photos/%Y/%m/%a/")
    facebook_link = models.U
