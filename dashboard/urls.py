from django.urls import path
from . import views
from dyingearthcode.views import homePage
urlpatterns = [
    path("dashboard/", views.mainPage, name="main"),
    path("home", homePage, name='HomePage'),

    path("register/", views.registerPage, name="register-page"),
    path("login/", views.loginPage, name="login-page"),
    path("logout/", views.logoutPage, name="logout-page"),

    path("profile/<str:pk>/", views.userProfile, name="user-profile"),
    path("settings/", views.settingsPage, name="profile-settings"),

    path("app-todo/", views.appTodo, name="app-todo"),

]
