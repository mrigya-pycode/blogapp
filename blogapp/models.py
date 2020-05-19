from django.db import models

# Create your models here

from datetime import datetime
class blog(models.Model):
    bloger_about=models.CharField(max_length=60)
    bloger_post=models.CharField(max_length=500)
    bloger_pic=models.FileField(upload_to='images/',default="")
    blogger_author=models.CharField(max_length=50,default="")
    blogger_date=models.DateTimeField(default=datetime.now(), blank=True)
    def __str__(self):
        return self.bloger_about
