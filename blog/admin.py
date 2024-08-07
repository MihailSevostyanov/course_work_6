from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'created_at', 'is_published', 'number_views')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')