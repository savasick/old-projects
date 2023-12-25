from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('account/<username>', views.account, name='account'),
    path('settings', views.account_edit, name="settings"),
    path("security", views.change_password, name="security"),
  ]

if bool(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
