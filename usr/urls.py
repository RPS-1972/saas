from django.urls import path
from . import views


urlpatterns = [

	
	path('', views.landing_page, name="landing_page"),

    path('dashboard/', views.home, name="home"),
    path('about/', views.contact),
    path('services/', views.services),

	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]