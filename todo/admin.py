from django.contrib import admin

from .models import TodoItem

# Register your models here.

class TodoItemAdmin(admin.ModelAdmin):
	fields = ['content', 'done', 'desc']

admin.site.register(TodoItem, TodoItemAdmin)