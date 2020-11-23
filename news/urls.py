from django.urls import path
from .views import APIPostDetail, APIPostList, PostList, TagList, APITagList, APITagDetail, PostDetail

urlpatterns = [

    path('api/post/<int:pk>', APIPostDetail.as_view()),
    path('api/posts', APIPostList.as_view()),

    path('api/tag/<int:pk>', APITagDetail.as_view()),
    path('api/tags', APITagList.as_view()),

    path('news', PostList.as_view()),
    path('post/<str:slug>', PostDetail.as_view()),

    path('tags', TagList.as_view()),

    ]
