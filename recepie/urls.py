from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static

from recepie.views import *
from recepie.forms import LoginForm

urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=LoginForm, redirect_authenticated_user=True), name="Login"),
    path('logout/', LogoutView.as_view(), name="Logout"),
    path('reset-password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup/', signup, name="Signup"),
    path('profile/', profile ,name="Profile"),
    path('profile/update/', update_profile, name="ProfileUpdate"),
    path('profile/update/password/', change_password, name="PasswordChange"),
    path('', HomePageView.as_view(), name="Home"),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], protected_serve, {'document_root': settings.MEDIA_ROOT}),
    path('export_users/', export_excel, name="ExportExcel"),
    path('api/', include('rest.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
