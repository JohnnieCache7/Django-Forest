from django.db import models

# Create your models here.
class best_seller(models.Model):
    book_name = models.CharField(max_length=400)
    author = models.CharField(max_length=100)
    ave_user_rating = models.FloatField()
    review_count = models.IntegerField()
    price = models.FloatField()
    year = models.IntegerField()
    genre = models.CharField(max_length=30)