from rest_framework import serializers

from .models import Link, LinkFollow
from .utils import create_short_link


class LinkSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    short_url = serializers.CharField(read_only=True)

    class Meta:
        model = Link
        fields = '__all__'

    def create(self, validated_data):
        short_url = create_short_link()
        self.validated_data['short_url'] = short_url
        validated_data['short_url'] = short_url
        return super().create(validated_data)


class LinkFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkFollow
        fields = ('ip', 'device', 'follow_time')
