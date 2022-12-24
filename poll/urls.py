from django.urls import path
from . import views

urlpatterns = [
    path("",views.signUPView, name="signup-view"),
    path("auth/login",views.user_Login, name="login-view"),
    path("auth/profile/",views.user_profile, name="profile-view"),
    path("auth/profile/delete/<int:pk>",views.delete_user_view, name="profile-edit-view"),
    path("auth/editprofile/<int:pk>", views.usereditview,name="edit-profile-view"),
]
