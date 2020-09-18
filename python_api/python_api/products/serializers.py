from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'code', 'product_type', 'cost', 'description', 'pushed_product', 'callback', 'category')
