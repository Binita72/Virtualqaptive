from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")


# Registering the model

admin.site.register(Todo, TodoAdmin)

