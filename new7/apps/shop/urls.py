from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'shop', views.ShopViewSet)
router.register(r'shop/income', views.ShopIncomeViewSet)

urlpatterns = router.urls
