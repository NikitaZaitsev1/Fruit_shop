from django.contrib import admin, messages
from django.utils.translation import ngettext

from home.models import FeedBack


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'active', 'created')
    list_filter = ('email', 'active', 'created')
    list_per_page = 10
    ordering = ['-created']
    actions = ['make_status_active', 'make_status_inactive']
    date_hierarchy = 'created'

    fieldsets = (
        (None, {
            'fields': ('full_name', 'email', 'phone', 'message')
        }),
    )

    @admin.action(description='Mark selected feedbacks as active')
    def make_status_active(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(request, ngettext(
            '%d feedback was successfully marked as moderated.',
            '%d feedbacks were successfully marked as moderated.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark selected feedbacks as inactive')
    def make_status_inactive(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(request, ngettext(
            '%d feedback was successfully marked as inactive.',
            '%d feedbacks were successfully marked as inactive.',
            updated,
        ) % updated, messages.WARNING)


admin.site.register(FeedBack, FeedBackAdmin)
