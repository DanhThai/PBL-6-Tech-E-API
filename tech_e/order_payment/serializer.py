
from django.forms import CharField
from rest_framework import serializers
from order_payment.models import Order, OrderDetail
from tech_ecommerce.models import CartItem, ProductChilds
from tech_ecommerce.serializers import CartItemSerializer, ProductChildSerializer 

class OrderDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderDetail
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product_child'] = ProductChildSerializer(instance.product_child).data
        return response
    def create(self, validated_data):
        return OrderDetail.objects.create(**validated_data)

class OrderSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer(many=True, required=False)
    cart_item_id = serializers.PrimaryKeyRelatedField(queryset=CartItem.objects.all(), write_only=True,many=True)
    class Meta:
        model = Order
        fields = '__all__'
    
    def create(self, validated_data):
        cart_items = validated_data.pop('cart_item_id')
        number_order = int(len(cart_items))
        order = Order.objects.create(
            user = validated_data.get('user'),
            total_price = 0,
            order_count = number_order,
            # discount = validated_data.get('discount'),
        )
        sub_price = 0
        for i in range(0, number_order):
            item = cart_items[i]
            child = ProductChilds.objects.get(pk=item.product_child_id)
            orderDetail = OrderDetail.objects.create(
                product_child = child, 
                order = order,
                quantity =  item.quantity,
                total_price =  item.total_price,
            )
            orderDetail.save()
            sub_price += item.total_price
        order.total_price = sub_price
        order.save()
        return order