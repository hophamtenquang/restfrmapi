from rest_framework import serializers

from .models import User, Post, Image


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedIdentityField(view_name='userpost-list')

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    images = serializers.HyperlinkedIdentityField(view_name='postimage-list')
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='author', write_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')
    # image_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = '__all__'
