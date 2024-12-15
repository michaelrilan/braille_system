from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.user_login, name="login"),
    path("register", views.register, name="register"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("tutorial", views.tutorial, name="tutorial"),
    path("download_confirm", views.download_confirm, name="download_confirm"),
    path("create_braille", views.create_braille, name="create_braille"),
    path('download_braille/<str:file_name>/', views.download_braille, name='download_braille'),
    path("view_braille", views.view_braille, name="view_braille"),
    path("archives", views.archives, name="archives"),
    path('manage_account',views.manage_account, name='manage_account'),
    path('list_of_student',views.list_of_student, name='list_of_student'),
    path("shared", views.shared, name="shared"),
    path("shared_braille", views.shared_braille, name="shared_braille"),
    path("account_settings", views.account_settings, name="account_settings"),
    path("logout_user", views.logout_user, name="logout_user"),
    path('grammar_check/',views.grammar_check, name='grammar_check'),
    path('filter_students_active/', views.filter_students_active, name='filter_students_active'),
    path('filter_students_disabled/', views.filter_students_disabled, name='filter_students_disabled'),

    path('upload_audio/', views.upload_audio, name='upload_audio'),
]