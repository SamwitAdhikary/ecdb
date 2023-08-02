from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=20, default='', unique=True)
    username = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + self.last_name
    
class UserAddress(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=100, default='')
    address_line_2 = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    postal_code = models.IntegerField(default=0)
    country = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user_id)
    
class UserPayment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100, default='')
    provider = models.CharField(max_length=100, default='')
    account_number = models.IntegerField(default=0)
    expiry_date = models.DateField()

    def __str__(self):
        return str(self.user_id)
    
class ProductCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=100, default='', unique=True)
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name
    
class ProductInventory(models.Model):
    id = models.CharField(primary_key=True, max_length=100, default='', unique=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
    
class Discount(models.Model):
    id = models.CharField(primary_key=True, max_length=100, default='', unique=True)
    name = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=500, default='')
    discount_percent = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=100, default='', unique=True)
    name = models.CharField(max_length=100, default='')
    description = models.TextField()
    sku = models.CharField(max_length=50, default='')
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    inventory_id = models.ForeignKey(ProductInventory, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class PaymentDetails(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    provider = models.CharField(max_length=10, default='')
    status = models.CharField(max_length=10, default='')

    def __str__(self):
        return str(self.id)
    
class OrderDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    payment_id = models.ForeignKey(PaymentDetails, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
    
class ShoppingSession(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
    
class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    session_id = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
    
