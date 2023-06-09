from django.urls import path
from django.contrib.auth import views as auth_views

from usersapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='usersapp/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usersapp/logout.html'), name = 'logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='usersapp/password_reset.html'), name = 'password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='usersapp/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='usersapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='usersapp/password_reset_complete.html'), name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('profil/', views.profil, name='profil')
]