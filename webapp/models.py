from django.db import models
from django.utils import timezone

# Create your models here.

class Candy(models.Model):
  flavor = models.CharField(max_length=100)
  description = models.TextField()
  manufacturedDate = models.DateTimeField('MFD', default=timezone.now())
  bestBefore = models.DateTimeField('BB', blank=True, null=True)

  def produce(self):
    self.bestBefore = timezone.now() + timezone.timedelta(days=30)

  def __str__(self):
    return self.flavor