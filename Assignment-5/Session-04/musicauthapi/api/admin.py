from django.contrib import admin
from .models import *

admin.site.register(Playlist)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Ticket)