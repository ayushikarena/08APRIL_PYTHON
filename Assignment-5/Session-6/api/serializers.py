import datetime
from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes custom validation to prevent setting a publication year in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Validates that the publication year is not in the future.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year ({value}) cannot be in the future. Current year is {current_year}."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes a nested list of BookSerializer instances representing the books written by this author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
