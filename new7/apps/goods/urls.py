from django.conf.urls import url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'goods', views.GoodsViewSet)
router.register(r'goodsrecord', views.GoodsRecordViewSet)
router.register(r'damaged', views.GoodsDamagedViewSet)

urlpatterns = router.urls
