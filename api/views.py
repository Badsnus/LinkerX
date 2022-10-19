from django import shortcuts, views
from rest_framework import viewsets, response, permissions

from .models import Link, LinkFollow
from .serializers import LinkSerializer, LinkFollowSerializer
from .permissions import IsOwnerOfLink


class LinksApiView(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()

    def get_permissions(self):
        if self.action in ('list', 'update'):
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [IsOwnerOfLink]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer_instance = self.get_serializer(instance)
        links_redirects = LinkFollow.objects.filter(link=instance).all()
        return response.Response(
            [{'link': serializer_instance.data,
              'link_follows': [LinkFollowSerializer(link).data for link in
                               links_redirects]}])


class LinkRedirect(views.generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        redirect_link = shortcuts.get_object_or_404(
            Link, short_url=kwargs['custom_url']
        )
        ip = (self.request.META.get("HTTP_X_FORWARDED_FOR", "").split(",")[0]
              or self.request.META.get("REMOTE_ADDR"))
        device = self.request.META.get("HTTP_USER_AGENT", "Unknown")[:300]
        LinkFollow.objects.create(ip=ip, device=device, link=redirect_link)
        self.url = redirect_link.long_url
        return super().get_redirect_url(*args, **kwargs)
