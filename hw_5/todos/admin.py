from django.contrib import admin # type: ignore
from .models import Todo

admin.site.register(Todo)
