from .models import CartItem, User, UserAddress, Discount, OrderDetails, OrderItems, PaymentDetails, Product, ProductCategory, ProductInventory, ShoppingSession, UserPayment
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'

class UserAddressSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField('getaddress')

    def getaddress(self, user):
        qs = UserAddress.objects.filter(user_id=user)
        serializer = AddressSerializer(instance=qs, many=True)
        return serializer.data
    
    class Meta:
        model = User
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = '__all__'

class UserPaymentSerializer(serializers.ModelSerializer):
    payment = serializers.SerializerMethodField('getpayment')

    def getpayment(self, user):
        qs = UserPayment.objects.filter(user_id=user)
        serializer = PaymentSerializer(instance=qs, many=True)
        return serializer.data
    
    class Meta:
        model = User
        fields = '__all__'

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'

class UserOrderDetailsSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField('getuserorder')

    def getuserorder(self, user):
        qs = OrderDetails.objects.filter(user_id=user)
        serializer = OrderDetailsSerializer(instance=qs, many=True)
        return serializer.data
    
    class Meta:
        model = User
        fields = '__all__'

class OrderItemsDetailsSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField('getorderitem')

    def getorderitem(self, order):
        qs = OrderItems.objects.filter(order_id=order)
        serializer = OrderItemsSerializer(instance=qs, many=True)
        return serializer.data
    
    class Meta:
        model = OrderDetails
        fields = '__all__'

class OrderProductSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField('getorderproduct')

    def getorderproduct(self, product):
        qs = OrderItems.objects.filter(product_id=product)
        serializer = OrderItemsSerializer(instance=qs, many=True)
        return serializer.data
    
    class Meta:
        model = Product
        fields = '__all__'

class ShoppingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingSession
        fields = '__all__'

class UserShoppingSessionSerializer(serializers.ModelSerializer):
    session = serializers.SerializerMethodField('getusersession')

    def getusersession(self, user):
        qs = ShoppingSession.objects.filter(user_id=user)
        serializer = ShoppingSessionSerializer(instance=qs, many=True)
        return serializer.data
    
    class Meta:
        model = User
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CartShoppingSessionSerializer(serializers.ModelSerializer):
    cart = serializers.SerializerMethodField('getcartsession')

    def getcartsession(self, session):
        qs = CartItem.objects.filter(session_id=session)
        serializer = CartItemSerializer(instance=qs, many=True)
        return serializer.data
    
    class Meta:
        model = ShoppingSession
        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):
    cart = serializers.SerializerMethodField('getcartproduct')

    def getcartproduct(self, product):
        qs = CartItem.objects.filter(product_id=product)
        serializer = CartItemSerializer(instance=qs, many=True)
        return serializer.data
    
    class Meta:
        model = Product
        fields = '__all__'