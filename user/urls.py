from django.urls import path

from . import views


urlpatterns = [
    # create account url
    path("register", views.register_request, name="register"),
    # login url
    path("login", views.login_request, name="login"),
    # logout url
    path("logout", views.logout_request, name="logout"),
    path('profile/<str:username>', views.profile, name='user_profile'),

]