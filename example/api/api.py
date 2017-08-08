from rest_framework import generics


from .serializers import UserSerializer, PostSerializer, ImageSerializer
from .models import User, Post, Image

import random


class UserMixin(object):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(UserMixin, generics.ListCreateAPIView):
    pass


class UserDetail(UserMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'


class PostMixin(object):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Force author to the current user on save"""
        authors = User.objects.all()
        index = random.randint(0, len(authors))
        auth = authors[index]

        auth = User.objects.get(username='admin')
        serializer.save(author=auth)


class PostList(PostMixin, generics.ListCreateAPIView):
    pass


class PostDetail(PostMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class UserPostList(generics.ListAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super(UserPostList, self).get_queryset()
        return queryset.filter(author__pk=self.kwargs.get('pk'))


class ImageMixin(object):
    model = Image
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageList(ImageMixin, generics.ListAPIView):
    pass


class ImageDetail(ImageMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class PostImageList(generics.ListAPIView):
    model = Image
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_queryset(self):
        queryset = super(PostImageList, self).get_queryset()
        return queryset.filter(post__pk=self.kwargs.get('pk'))
