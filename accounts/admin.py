from django.contrib import admin
from .models import user, ticket

admin.site.register(user)
admin.site.register(ticket)