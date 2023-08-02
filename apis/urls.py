from . import viewsets

from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

router.register('user', viewsets.UserViewSet)
router.register('address', viewsets.AddressViewSet)
router.register('useraddress', viewsets.UserAdddressViewSet)
router.register('payment😎', viewsets.PaymentViewSet)
router.register('userpayment🤑', viewsets.UserPaymentViewSet)
router.register('productcategory', viewsets.ProductCategoryViewSet)
router.register('productinventory', viewsets.ProductInventoryViewSet)
router.register('discount', viewsets.DiscountViewSet)
router.register('product', viewsets.ProductViewSet)
router.register('paymentdetails', viewsets.PaymentDetailsViewSet)
router.register('orderdetails', viewsets.OrderDetailsViewSet)
router.register('userorder', viewsets.UserOrderViewSet)
router.register('orderitems', viewsets.OrderItemsViewSet)
router.register('orderitemdetails', viewsets.OrderItemsDetailsViewSet)
router.register('orderproduct', viewsets.OrderProductViewSet)
router.register('shoppingsession', viewsets.ShoppingSessionViewSet)
router.register('usershoppingsession', viewsets.UserShoppingSessionViewSet)
router.register('cartitem', viewsets.CartItemViewSets)
router.register('cartshoppingsession', viewsets.CartShoppingSessionViewSet)
router.register('cartproduct', viewsets.CartProductViewSet)


urlpatterns = [
    path('', include(router.urls))
]