from django.conf.urls import url, include

from .api import UserList, UserDetail, UserPostList
from .api import PostList, PostDetail, PostImageList
from .api import ImageList, ImageDetail, ImageAPIView

user_urls = [
    url(r'^$', UserList.as_view(), name='user-list'),
    url(r'^/(?P<pk>\d+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^/(?P<pk>\d+)/posts$', UserPostList.as_view(), name='userpost-list')
]

post_urls = [
    url(r'^$', PostList.as_view(), name='post-list'),
    url(r'^/(?P<pk>\d+)$', PostDetail.as_view(), name='post-detail'),
    url(r'^/(?P<pk>\d+)/images$', PostImageList.as_view(), name='postimage-list')
]

image_urls = [
    url(r'^$', ImageList.as_view(), name='image-list'),
    url(r'^/(?P<pk>\d+)$', ImageDetail.as_view(), name='image-detail'),
    url(r'^/add$', ImageAPIView.as_view(), name='image-add')
]

urlpatterns = [
    url(r'^users', include(user_urls)),
    url(r'^posts', include(post_urls)),
    url(r'^images', include(image_urls)),
]
