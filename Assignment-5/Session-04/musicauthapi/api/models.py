from django.db import models


class Playlist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    food_name = models.CharField(max_length=100)

    def __str__(self):
        return self.food_name


class Cart(models.Model):
    product = models.CharField(max_length=100)

    def __str__(self):
        return self.product


class Ticket(models.Model):
    movie = models.CharField(max_length=100)

    def __str__(self):
        return self.movie