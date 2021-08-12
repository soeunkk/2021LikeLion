from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Review(models.Model): #User와 다대다 관계(중개모델:Scrap), Comment와 일대다 관계
    restaurant = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(null=True)
    food_image = models.ImageField(upload_to='images/', null=True)
    users_scrap = models.ManyToManyField(User, related_name="scrapped_review", through="Scrap")
    users_like = models.ManyToManyField(User, related_name="liked_review", through="Like")

    def __str__(self):
        return self.restaurant

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)