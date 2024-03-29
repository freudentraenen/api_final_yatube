from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet
from .views import CommentViewSet, FollowViewSet


app_name = 'api'

router_v1 = SimpleRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'groups', GroupViewSet)
router_v1.register(
    r'posts\/(?P<post_id>\d+)\/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(
    r'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
