from django.contrib import admin
from .models import TodoItem

# Register your models here.
admin.site.site_header = 'My portfolio'

admin.site.register(TodoItem)