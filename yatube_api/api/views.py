from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from .permissions import IsAuthorPermission
from .permissions import UserOrReadOnly
from posts.models import Post, Group, Follow
from .serializers import PostSerializer, GroupSerializer
from .serializers import FollowSerializer, CommentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ('get')
    permission_classes = (AllowAny,)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorPermission,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        comments = post.comments
        return comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            return (IsAuthenticated(),)
        return super().get_permissions()


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (UserOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = self.request.user
        followings = user.follower
        return followings

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
