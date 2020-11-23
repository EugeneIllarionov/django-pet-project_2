from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, View
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer
from rest_framework.pagination import PageNumberPagination


class APIPostDetail(APIView):
    serializer_class = PostSerializer

    def get(self, request, pk, format=None):
        obj = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(obj, context={'request': request})
        return Response(serializer.data)


class PostPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class APIPostList(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    queryset = Post.objects.all()


class PostList(ListView):
    template = 'post_list.html'

    def get(self, request, **kwargs):
        return render(request, self.template)


class PostDetail(View):
    template = 'post_list.html'

    def get(self, request, slug, **kwargs):
        return render(request, self.template)


class APITagList(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class APITagDetail(APIView):
    serializer_class = TagSerializer

    def get(self, request, pk, format=None):
        obj = get_object_or_404(Tag, pk=pk)
        serializer = TagSerializer(obj)
        return Response(serializer.data)


class TagList(ListView):
    template = 'tag_list.html'

    def get(self, request, **kwargs):
        return render(request, self.template)




