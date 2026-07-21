from django.contrib import admin
from .models import *


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):

    def has_view_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

    def has_add_permission(self, request):
        return request.user.groups.filter(name='Admin').exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name='Admin').exists()

admin.site.register(Product)
admin.site.register(Review)