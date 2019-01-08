from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'shop', views.ShopViewSet)
router.register(r'income', views.ShopIncomeViewSet)
router.register(r'inventory', views.ShopInventoryViewSet)

urlpatterns = router.urls
