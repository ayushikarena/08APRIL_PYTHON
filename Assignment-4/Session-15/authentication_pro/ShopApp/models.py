from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.title
    
class Review(models.Model):
    movie=models.CharField(max_length=100)
    review=models.TextField()

    def __str__(self):
        return self.movie
    
#===================Task-5====================
class Playlist(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name