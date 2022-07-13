from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=350, default='', blank=True, null=True)
    image = models.ImageField(upload_to='marketplace/%Y/%m/%d/')
    moderated = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
