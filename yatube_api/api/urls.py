from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import PostViewSet, GroupViewSet
from .views import CommentViewSet, FollowViewSet


app_name = 'api'

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(
    r'posts\/(?P<post_id>\d+)\/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    r'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
