from rest_framework import generics, status, views


from .serializers import UserSerializer, PostSerializer, ImageSerializer
from .models import User, Post, Image
from rest_framework.response import Response


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
        serializer.save(author=self.request.user)


class PostList(PostMixin, generics.ListCreateAPIView):
    def post(self, request, format=None):
        serializer = PostSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(PostMixin, generics.RetrieveUpdateDestroyAPIView):
    def put(self, request, pk, format=None):
        instance = self.get_object()
        serializer = PostSerializer(instance, data=self.request.data, context={'request': self.request})
        import pdb; pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class ImageAPIView(views.APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, format, request=None):
        post_id = self.request.data['post_id']
        create_post = Post.objects.all().filter(id=post_id).get()
        image = self.request.FILES.get('file')
        obj = Image.objects.create(post=create_post)
        obj.image = image
        obj.save()
        # import pdb; pdb.set_trace()
        return Response(status=status.HTTP_202_ACCEPTED)
