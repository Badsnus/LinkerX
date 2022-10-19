from rest_framework import serializers

from .models import Link, LinkFollow
from .utils import create_custom_url
from .validators import length_validator


class LinkSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    custom_url = serializers.CharField(read_only=True)
    length_url = serializers.IntegerField(validators=(length_validator,))

    class Meta:
        model = Link
        fields = '__all__'

    def create(self, validated_data):
        length = validated_data['length_url']
        custom_url = create_custom_url(length)
        self.validated_data['custom_url'] = custom_url
        validated_data['custom_url'] = custom_url

        return super().create(validated_data)


class LinkFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkFollow
        fields = ('ip', 'device', 'follow_time')
