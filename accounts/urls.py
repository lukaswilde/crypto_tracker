from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import BootstrapAuthenticationForm

app_name = "accounts"
urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html",
            next_page="prices:index",
            authentication_form=BootstrapAuthenticationForm,
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="pages:index"),
        name="logout",
    ),
]
