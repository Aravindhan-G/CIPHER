from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index, name = "Base"),
    path('home',views.Login, name = "Home"),
    path('signup', views.SignUp, name = "SignUp"),
    path('Home', views.Transfer, name = 'Home'),
    path('update', views.Update, name='Update'),
    path('logout', views.Logout, name='Logout'),
    path('friends', views.Friends, name='friends'),
    path('change_friends', views.Change_Friends, name='change_friends'),
    path('return', views.Return, name='Return'),
    path('usage_chart', views.usage_chart, name='usage_chart'),
    path('dashboard', views.Dash, name='Dashboard')
]