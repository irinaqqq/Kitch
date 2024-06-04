from django.urls import path, include, re_path
from rest_framework import routers
from rest.views import UserViewSet, PostViewSet, api_root

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    # Uncomment and update these URLs if necessary
    # re_path(r'^posts/$', PostsList.as_view(), name="Posts"),
    # re_path(r'^posts/(?P<pk>\d+)/$', PostDetails.as_view(), name="PostDetails"),
    # re_path(r'^users/$', UsersList.as_view(), name="Users"),
    # re_path(r'^users/(?P<pk>\d+)/$', UserDetails.as_view(), name="UserDetails")
]

# Uncomment the following line if you're using format_suffix_patterns
# from rest_framework.urlpatterns import format_suffix_patterns
# urlpatterns = format_suffix_patterns(urlpatterns)
