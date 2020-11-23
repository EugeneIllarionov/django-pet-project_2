from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from profiles.models import CustomUser


class ProfilesSerializer(ModelSerializer):
    avatar_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = CustomUser
        first_name = serializers.CharField()
        fields = ('first_name',
                  'last_name',
                  'bio',
                  'location',
                  'avatar',
                  'avatar_thumbnail'
                  )


class ProfileComment(ModelSerializer):
    avatar_thumbnail = serializers.ImageField(read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='api-profile')

    class Meta:
        model = CustomUser
        first_name = serializers.CharField()
        fields = ('first_name',
                  'last_name',
                  'avatar_thumbnail',
                  'link'
                  )
