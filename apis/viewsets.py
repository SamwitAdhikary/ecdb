from rest_framework import viewsets
from . import serializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = serializer.User.objects.all()
    serializer_class = serializer.UserSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = serializer.UserAddress.objects.all()
    serializer_class = serializer.AddressSerializer

class UserAdddressViewSet(viewsets.ModelViewSet):
    queryset = serializer.User.objects.all()
    serializer_class = serializer.UserAddressSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = serializer.UserPayment.objects.all()
    serializer_class = serializer.PaymentSerializer

class UserPaymentViewSet(viewsets.ModelViewSet):
    queryset = serializer.User.objects.all()
    serializer_class = serializer.UserPaymentSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = serializer.ProductCategory.objects.all()
    serializer_class = serializer.ProductCategorySerializer

class ProductInventoryViewSet(viewsets.ModelViewSet):
    queryset = serializer.ProductInventory.objects.all()
    serializer_class = serializer.ProductInventorySerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = serializer.Discount.objects.all()
    serializer_class = serializer.DiscountSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = serializer.Product.objects.all()
    serializer_class = serializer.ProductSerializer

class PaymentDetailsViewSet(viewsets.ModelViewSet):
    queryset = serializer.PaymentDetails.objects.all()
    serializer_class = serializer.PaymentDetailsSerializer

class OrderDetailsViewSet(viewsets.ModelViewSet):
    queryset = serializer.OrderDetails.objects.all()
    serializer_class = serializer.OrderDetailsSerializer

class UserOrderViewSet(viewsets.ModelViewSet):
    queryset = serializer.User.objects.all()
    serializer_class = serializer.UserOrderDetailsSerializer

class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = serializer.OrderItems.objects.all()
    serializer_class = serializer.OrderItemsSerializer

class OrderItemsDetailsViewSet(viewsets.ModelViewSet):
    queryset = serializer.OrderDetails.objects.all()
    serializer_class = serializer.OrderItemsDetailsSerializer

class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = serializer.Product.objects.all()
    serializer_class = serializer.OrderProductSerializer

class ShoppingSessionViewSet(viewsets.ModelViewSet):
    queryset = serializer.ShoppingSession.objects.all()
    serializer_class = serializer.ShoppingSessionSerializer

class UserShoppingSessionViewSet(viewsets.ModelViewSet):
    queryset = serializer.User.objects.all()
    serializer_class = serializer.UserShoppingSessionSerializer

class CartItemViewSets(viewsets.ModelViewSet):
    queryset = serializer.CartItem.objects.all()
    serializer_class = serializer.CartItemSerializer

class CartShoppingSessionViewSet(viewsets.ModelViewSet):
    queryset = serializer.ShoppingSession.objects.all()
    serializer_class = serializer.CartShoppingSessionSerializer

class CartProductViewSet(viewsets.ModelViewSet):
    queryset = serializer.Product.objects.all()
    serializer_class = serializer.CartProductSerializer