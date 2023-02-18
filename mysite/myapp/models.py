from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    def __str__(self):
        return "{0}".format(self.name)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=300)
    price=models.IntegerField()
    book_image=models.ImageField(default='default.jpg',upload_to='book_images/')

class Task(models.Model):
    def __str__(self):
        return "{0}".format(self.name)
    name=models.CharField(max_length=100, default='')
    desc=models.CharField(max_length=300, default='')
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField(default=timezone.now().time())
    end_time = models.TimeField(default=timezone.now().time())