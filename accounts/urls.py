from django.urls import path
from .views import loginView, SignUpView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", loginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path(
        "logout/", LogoutView.as_view(template_name="space/index.html"), name="logout"
    ),
]