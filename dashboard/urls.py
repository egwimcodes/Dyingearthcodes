from django.urls import path, include
from . import views
from .views import UserCreationView, AccountDeleteView, SettingsView, CustomPasswordChangeView, UserSensorsView, DashboardView, RegisterNewSensorView
from dyingearthcode.views import homePage

urlpatterns = [
    path("home", homePage, name='HomePage'),
    path('accounts/password_change/',
         CustomPasswordChangeView.as_view(), name="password_change"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path('accounts/<pk>/delete/', AccountDeleteView.as_view(), name="account_delete"),
    path("register/", UserCreationView.as_view(), name="register"),
    path("sensors/<str:pk>/", UserSensorsView.as_view(), name="sensors"),
    path("settings/<int:user_id>/", SettingsView.as_view(), name="settings"),
    path("register_new_sensor/<pk>/", RegisterNewSensorView.as_view(), name='register_new_sensor'),

    path("app-todo/", views.appTodo, name="app-todo"),

]
