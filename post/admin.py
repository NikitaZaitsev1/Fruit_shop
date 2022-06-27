from django.contrib import admin
from post.models import Post, Tag


class AdminPosts(admin.ModelAdmin):
    list_display = ("author", "title", "photo","created_date", "published_date")


admin.site.register(Post, AdminPosts)


class AdminTags(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Tag, AdminTags)
