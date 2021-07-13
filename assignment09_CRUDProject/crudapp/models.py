from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.
class Review(models.Model):
    restaurant = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(null=True)
    food_image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.restaurant

