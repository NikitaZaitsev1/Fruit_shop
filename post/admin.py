from django.contrib import admin, messages
from django.utils.translation import ngettext

from post.models import Post, Tag


class AdminPosts(admin.ModelAdmin):
    list_display = ("author", "title", "photo", "created_date", "published_date", "is_published")
    list_filter = ('author', 'title', 'created_date', 'is_published')
    list_per_page = 10
    ordering = ['-created_date']
    actions = ['make_status_published', 'make_status_unpublished']
    date_hierarchy = 'published_date'

    fieldsets = (
        (None, {
            'fields': ('author', 'title', 'text', 'photo', 'created_date', 'tag')
        }),
    )

    @admin.action(description='Mark selected posts as published')
    def make_status_published(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, ngettext(
            '%d post was successfully marked as published.',
            '%d posts were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark selected posts as unpublished')
    def make_status_unpublished(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, ngettext(
            '%d post was successfully marked as unpublished.',
            '%d posts were successfully marked as unpublished.',
            updated,
        ) % updated, messages.WARNING)


admin.site.register(Post, AdminPosts)


class AdminTags(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Tag, AdminTags)
