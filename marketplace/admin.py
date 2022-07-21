from django.contrib import admin, messages
from django.utils.translation import ngettext

from marketplace.models import Product, Category


class AdminProducts(admin.ModelAdmin):
    list_display = ("seller", "name", "price", "moderated", "created_date", "published_date")
    list_filter = ('name', 'moderated')
    list_per_page = 10
    ordering = ['-created_date']
    actions = ['make_status_moderated', 'make_status_unmoderated']
    date_hierarchy = 'created_date'

    fieldsets = (
        (None, {
            'fields': ('seller', 'name', 'price', 'description', 'image', 'created_date', 'category')
        }),
    )

    @admin.action(description='Mark selected products as moderated')
    def make_status_moderated(self, request, queryset):
        updated = queryset.update(moderated=True)
        self.message_user(request, ngettext(
            '%d product was successfully marked as moderated.',
            '%d products were successfully marked as moderated.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark selected products as unmoderated')
    def make_status_unmoderated(self, request, queryset):
        updated = queryset.update(moderated=False)
        self.message_user(request, ngettext(
            '%d product was successfully marked as unmoderated.',
            '%d products were successfully marked as unmoderated.',
            updated,
        ) % updated, messages.WARNING)


class AdminCategories(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Product, AdminProducts)
admin.site.register(Category, AdminCategories)
