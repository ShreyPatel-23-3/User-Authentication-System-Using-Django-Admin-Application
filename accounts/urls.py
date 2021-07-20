from django.urls import path
from accounts import views


urlpatterns = [
    path("", views.login_page),
    path("register", views.register_page),
    path("index", views.index)
]
