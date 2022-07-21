from django.contrib import admin, messages
from django.utils.translation import ngettext

from order.models import Order


class AdminOrder(admin.ModelAdmin):
    list_display = ('product', 'customer', 'address', 'phone', 'date', 'processed')
    list_filter = ('product', 'customer', 'date', 'processed')
    list_per_page = 10
    ordering = ['-date']
    actions = ['make_status_processed', 'make_status_unprocessed']
    date_hierarchy = 'date'

    fieldsets = (
        (None, {
            'fields': ('product', 'customer', 'address', 'phone', 'date')
        }),
    )

    @admin.action(description='Mark selected orders as processed')
    def make_status_processed(self, request, queryset):
        updated = queryset.update(processed=True)
        self.message_user(request, ngettext(
            '%d order was successfully marked as processed.',
            '%d orders were successfully marked as processed.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark selected orders as unprocessed')
    def make_status_unprocessed(self, request, queryset):
        updated = queryset.update(processed=False)
        self.message_user(request, ngettext(
            '%d order was successfully marked as unprocessed.',
            '%d orders were successfully marked as unprocessed.',
            updated,
        ) % updated, messages.WARNING)


admin.site.register(Order, AdminOrder)
