from django.urls import path, include, re_path
from rest_framework import routers

from .views import LinksApiView, LinkRedirect

router = routers.SimpleRouter()
router.register(r'links', LinksApiView, basename='links')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
    path('<str:custom_url>/', LinkRedirect.as_view()),
]
