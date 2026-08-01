from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    comment = models.TextField()

    def __str__(self):
        return self.comment