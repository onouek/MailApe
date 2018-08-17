from django.contrib.auth import get_user_model
from rest_framework import serializers

from mailinglist.models import MailingList


class MailingListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all())

    class Meta:
        model = MailingList
        fields = ('url', 'id', 'name', 'owner', 'subscriber_set')
        read_only_fields = ('subscriber_set', )
        extra_kwargs = {
            'url': {'view_name': 'mailinglist:api-mailing-list-detail'},
            'subscriber_set': {'view_name': 'mailinglist:api-subscriber-detail'},
        }