from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
) 

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
  
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_meal_display()} on {self.date} for {self.finch}"
  class Meta:
    ordering = ['-date']

