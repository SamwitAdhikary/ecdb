from django.contrib import admin
from .models import CartItem, OrderDetails, Discount, OrderItems, PaymentDetails, Product, ProductCategory, UserPayment, ProductInventory, ShoppingSession, User, UserAddress

# Register your models here.

admin.site.register(CartItem)
admin.site.register(OrderDetails)
admin.site.register(Discount)
admin.site.register(OrderItems)
admin.site.register(PaymentDetails)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(UserPayment)
admin.site.register(ProductInventory)
admin.site.register(ShoppingSession)
admin.site.register(User)
admin.site.register(UserAddress)