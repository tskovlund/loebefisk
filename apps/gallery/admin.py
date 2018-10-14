from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'author']}),
        ('Date Information', {'fields': ['pub_date']}),
        ('Media', {'fields': ['image']}),
    ]
    list_display = ('title', 'pub_date', 'image')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
