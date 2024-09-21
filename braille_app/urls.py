from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("register", views.register, name="register"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("tutorial", views.tutorial, name="tutorial"),
    path("create_braille", views.create_braille, name="create_braille"),
    path('download_braille/<str:file_name>/', views.download_braille, name='download_braille'),
    path("view_braille", views.view_braille, name="view_braille"),
    path("archives", views.archives, name="archives"),
    path('manage_account',views.manage_account, name='manage_account'),
    path("shared", views.shared, name="shared"),
    path("account_settings", views.account_settings, name="account_settings"),
    path("logout_user", views.logout_user, name="logout_user"),
    path('grammar_check/',views.grammar_check, name='grammar_check'),

]