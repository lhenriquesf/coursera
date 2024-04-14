from rest_framework import serializers
from .models import Book
from decimal import Decimal

class BookSerializer(serializers.Hi):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = Book
        fields = ['id','title','author','price','stock','price_after_tax']

    def calculate_tax(self, product:Book):
        #return product.price*1.1 if 'price' in product else None
        price = product.get('price')
        if price is not None:
            return '{:.2f}'.format(price * Decimal(1.1))
        return None