from django.urls import path, include, re_path
from rest_framework import routers

from .views import LinksApiView, LinkRedirect

router = routers.SimpleRouter()
router.register(r'links', LinksApiView, basename='links')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('<str:short_url>/', LinkRedirect.as_view()),
]
