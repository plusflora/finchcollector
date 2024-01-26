from django.db import models
from django.urls import reverse
# Create your models here.

# finch model
class Finch(models.Model):
  species = models.CharField(max_length=100)
  population = models.CharField(max_length=50)
  habitat = models.CharField(max_length=100)
  about = models.TextField(max_length=250)
  def __str__(self):
    return self.species
  def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})
#