import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Test suite for the Book API endpoints.
    Covers CRUD operations, custom validation, authentication, custom permissions,
    filtering, searching, and ordering.
    """

    def setUp(self):
        # Create test users
        self.user_owner = User.objects.create_user(username='owner_user', password='password123')
        self.user_other = User.objects.create_user(username='other_user', password='password123')

        # Create test authors
        self.author_1 = Author.objects.create(name="George Orwell")
        self.author_2 = Author.objects.create(name="J.K. Rowling")

        # Create test books
        self.book_1 = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author_1,
            owner=self.user_owner
        )
        self.book_2 = Book.objects.create(
            title="Animal Farm",
            publication_year=1945,
            author=self.author_1,
            owner=self.user_owner
        )
        self.book_3 = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            publication_year=1997,
            author=self.author_2,
            owner=self.user_other
        )

        # Clients
        self.client_anonymous = APIClient()
        
        self.client_owner = APIClient()
        self.client_owner.login(username='owner_user', password='password123')
        
        self.client_other = APIClient()
        self.client_other.login(username='other_user', password='password123')

    def test_list_books(self):
        """Test listing books is public (anonymous users allowed)."""
        url = reverse('book-list')
        response = self.client_anonymous.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that we received results (using paginated format 'results')
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 3)

    def test_retrieve_book(self):
        """Test retrieving a single book details is public."""
        url = reverse('book-detail', kwargs={'pk': self.book_1.pk})
        response = self.client_anonymous.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create a book."""
        url = reverse('book-create')
        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author_1.id
        }
        response = self.client_anonymous.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """Test that authenticated users can create a book and owner is set automatically."""
        url = reverse('book-create')
        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author_1.id
        }
        response = self.client_owner.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Homage to Catalonia")
        
        # Verify owner is set correctly to user_owner
        created_book = Book.objects.get(title="Homage to Catalonia")
        self.assertEqual(created_book.owner, self.user_owner)

    def test_create_book_future_year_validation(self):
        """Test that validation fails when publication_year is in the future."""
        url = reverse('book-create')
        future_year = datetime.date.today().year + 1
        data = {
            "title": "Future Book",
            "publication_year": future_year,
            "author": self.author_1.id
        }
        response = self.client_owner.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)

    def test_update_book_by_owner(self):
        """Test that the owner of a book can update it."""
        url = reverse('book-update', kwargs={'pk': self.book_1.pk})
        data = {
            "title": "1984 - Modern Edition",
            "publication_year": 1950,
            "author": self.author_1.id
        }
        response = self.client_owner.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984 - Modern Edition")
        
        # Verify change in DB
        self.book_1.refresh_from_db()
        self.assertEqual(self.book_1.title, "1984 - Modern Edition")

    def test_update_book_by_non_owner(self):
        """Test that a non-owner cannot update a book (should return 403 Forbidden)."""
        url = reverse('book-update', kwargs={'pk': self.book_1.pk})
        data = {
            "title": "1984 - Hacked Edition",
            "publication_year": 1949,
            "author": self.author_1.id
        }
        response = self.client_other.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_by_owner(self):
        """Test that the owner of a book can delete it."""
        url = reverse('book-delete', kwargs={'pk': self.book_1.pk})
        response = self.client_owner.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book_1.pk).exists())

    def test_delete_book_by_non_owner(self):
        """Test that a non-owner cannot delete a book."""
        url = reverse('book-delete', kwargs={'pk': self.book_1.pk})
        response = self.client_other.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Book.objects.filter(pk=self.book_1.pk).exists())

    def test_filtering_books(self):
        """Test filtering books by publication_year and author."""
        url = reverse('book-list')
        
        # Filter by publication year
        response = self.client_anonymous.get(url, {'publication_year': 1945})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], "Animal Farm")

    def test_searching_books(self):
        """Test searching books by title or author name."""
        url = reverse('book-list')
        
        # Search for title containing "Sorcerer"
        response = self.client_anonymous.get(url, {'search': 'Sorcerer'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], "Harry Potter and the Sorcerer's Stone")

        # Search for author's name "Orwell"
        response = self.client_anonymous.get(url, {'search': 'Orwell'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_ordering_books(self):
        """Test ordering books by title and publication_year."""
        url = reverse('book-list')
        
        # Order by publication year ascending
        response = self.client_anonymous.get(url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles_asc = [book['title'] for book in response.data['results']]
        self.assertEqual(titles_asc, ["Animal Farm", "1984", "Harry Potter and the Sorcerer's Stone"])

        # Order by publication year descending
        response = self.client_anonymous.get(url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles_desc = [book['title'] for book in response.data['results']]
        self.assertEqual(titles_desc, ["Harry Potter and the Sorcerer's Stone", "1984", "Animal Farm"])
