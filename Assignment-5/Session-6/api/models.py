from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=150, help_text="The name of the author.")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250, help_text="The title of the book.")
    publication_year = models.IntegerField(help_text="The year the book was published.")
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name="books",
        help_text="The author of the book."
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="books_owned",
        null=True,
        blank=True,
        help_text="The user who registered/owns this book record."
    )

    def __str__(self):
        return self.title
