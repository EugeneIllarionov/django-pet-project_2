from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from news.models import Post, Comment, Tag
from profiles.serializers import ProfileComment


class CommentSerializer(ModelSerializer):
    author = ProfileComment(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(ModelSerializer):

    def get_like_count(self, obj):
        return obj.likes.count()

    image_thumbnail = serializers.ImageField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    pub_date = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    tags = TagSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'




