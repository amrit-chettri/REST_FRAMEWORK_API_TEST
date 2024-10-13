from rest_framework import serializers
from .models import Lead , Products , Orders

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
         model = Products
         fields = ('name', 'price','description')        


class OrderSerializer(serializers.ModelSerializer):
    class Meta:

        model = Orders
        fields = ('quantity', 'total_price')
