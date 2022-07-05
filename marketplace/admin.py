from django.contrib import admin

from marketplace.models import Product, Category


class AdminProducts(admin.ModelAdmin):
    list_display = ("seller", "name", "image", "moderated","created_date", "published_date")


class AdminCategories(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Product, AdminProducts)
admin.site.register(Category, AdminCategories)
