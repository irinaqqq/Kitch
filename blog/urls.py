from django.urls import path, re_path
from blog.views import *

urlpatterns = [
    path('posts/', display_posts, name="DisplayPosts"),
    path('posts/create/', PostCreateView.as_view(), name="CreatePost"),
    path('post/delete/', delete_post, name="DeletePost"),
    re_path(r'^post/(?P<post_id>\d+)/$', display_post, name="DisplayPost"),
    re_path(r'^post/(?P<post_id>\d+)/update/$', PostUpdateView.as_view(), name="UpdatePost"),
    # re_path(r'^post/(?P<post_id>\d+)/print/$', print_post, name="PrintPost"),
    path('post/<int:post_id>/preview/', print_preview, name="PrintPreview")
]
