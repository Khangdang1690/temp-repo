from django.db import models
from datetime import datetime

# Create your models here.
class Story(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  image = models.ImageField()
  tags = models.CharField(max_length=100)
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longtitude = models.DecimalField(max_digits=9,decimal_places=6)
  created_at = models.DateTimeField(default=datetime.now, blank=True)