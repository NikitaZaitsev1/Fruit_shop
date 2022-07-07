from django.contrib import admin

from order.models import Order


class AdminOrder(admin.ModelAdmin):
    list_display = ('product', 'customer', 'address', 'phone', 'date', 'status')


admin.site.register(Order, AdminOrder)
