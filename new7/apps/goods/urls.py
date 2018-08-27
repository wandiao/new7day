from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'goods', views.GoodsViewSet)

urlpatterns = router.urls
