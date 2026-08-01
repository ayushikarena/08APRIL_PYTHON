from rest_framework import generics, permissions, filters
from django_filters import rest_framework as django_filters
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .permissions import IsOwnerOrReadOnly

# --- Author Views ---

class AuthorListView(generics.ListCreateAPIView):
    """
    View to list all authors (GET) or create a new author (POST).
    Read access is open to all users. Write access is restricted to authenticated users.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a specific author instance.
    Read access is open to all users. Write/Delete access is restricted to authenticated users.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# --- Book Views ---

class BookListView(generics.ListAPIView):
    """
    View to retrieve a list of books.
    Provides advanced query capabilities:
    - Filtering: ?title=<val>&author__name=<val>&publication_year=<val>
    - Searching: ?search=<query> (searches title and author's name)
    - Ordering: ?ordering=<field> (supports ordering by title, publication_year)
    Read access is public.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    # Configure filtering, searching, and ordering backends
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering


class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve details of a single book.
    Read access is public.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    View to create a new Book record.
    Enforces authentication. Automatically maps the authenticated user as the owner.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Save the current authenticated user as the owner
        serializer.save(owner=self.request.user)


class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing Book record.
    Enforces authentication and checks that the user is the owner of the record.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a Book record.
    Enforces authentication and checks that the user is the owner of the record.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
