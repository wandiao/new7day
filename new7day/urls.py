"""new7day URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
# from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
   openapi.Info(
      title="新七天接口文档",
      default_version='v1',
      description="新七天接口文档",
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(AllowAny,),
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', schema_view.with_ui('swagger', cache_timeout=0), name='新七天接口文档'),
    url(r'^docs_ex/', include_docs_urls(title='My API title')),
    url(r'^auth/', include(('new7.apps.auth.urls','auth'), namespace='auth')),
    url(r'^account/', include(('new7.apps.account.urls','account'), namespace='account')),
    url(r'^order/', include(('new7.apps.order.urls','order'), namespace='order')),
    url(r'^supplier/', include(('new7.apps.supplier.urls','supplier'), namespace='supplier')),
    url(r'^client/', include(('new7.apps.client.urls','client'), namespace='client')),
    url(r'^depot/', include(('new7.apps.depot.urls','depot'), namespace='depot')),
    url(r'^goods/', include(('new7.apps.goods.urls','goods'), namespace='goods')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
