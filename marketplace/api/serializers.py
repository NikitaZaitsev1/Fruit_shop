from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from marketplace.models import Product


class ProductSerializer(ModelSerializer):
    seller = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image', 'category', 'seller')
