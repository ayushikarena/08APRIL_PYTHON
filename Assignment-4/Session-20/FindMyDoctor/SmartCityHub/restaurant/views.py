from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Restaurant

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        cuisine = self.request.GET.get('cuisine')
        location = self.request.GET.get('location')

        if cuisine:
            queryset = queryset.filter(cuisine__icontains=cuisine)
        if location:
            queryset = queryset.filter(location__icontains=location)
            
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cuisine'] = self.request.GET.get('cuisine', '')
        context['location'] = self.request.GET.get('location', '')
        return context

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant_detail.html'
    context_object_name = 'restaurant'
