from django.contrib import admin

# Register your models here.

from blog.models import Tag, Post, Comment, AuthorProfile
admin.site.register(Tag)
admin.site.register(AuthorProfile)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')
    #exclude = ["slug"]
admin.site.register(Post, PostAdmin)
