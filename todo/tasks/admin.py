from django.contrib import admin
from .models import Category, Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'priority', 'deadline', 'done')
    search_fields = ('title',)
    list_filter = ('done', 'deadline', 'category', 'priority')


admin.site.register(Task, TaskAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
