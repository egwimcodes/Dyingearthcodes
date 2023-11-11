from django.urls import path, include
from . import views
from .views import UserCreationView, AccountDeleteView, SettingsView, CustomPasswordChangeView
from dyingearthcode.views import homePage

urlpatterns = [
    path("home", homePage, name='HomePage'),
    path('accounts/password_change/', CustomPasswordChangeView.as_view(), name="password_change"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("dashboard/", views.mainPage, name="dashboard"),
    path('accounts/<pk>/delete/', AccountDeleteView.as_view(), name="account_delete"),
    path("register/", UserCreationView.as_view(), name="register"),
    path("profile/<str:pk>/", views.userProfile, name="user-profile"),
    path("settings/<int:user_id>/", SettingsView.as_view(), name="settings"),
    path('sensor-add/', views.sensorAddView, name='add-sensor'),

    path("app-todo/", views.appTodo, name="app-todo"),

]
