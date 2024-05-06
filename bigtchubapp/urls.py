from django.urls import path

from . import views

urlpatterns=[
	path('', views.home, name="home"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name="contact"),
	path('plutopay/', views.plutopay, name="plutopay"),
	path('realtorscanonwebsite/', views.realtorscanonwebsite, name="realtorscanonwebsite"),
	path('realtorscanon/', views.realtorscanon, name="realtorscanon"),
	path('infringobuy/', views.infringobuy, name="infringobuy"),
	path('fancreo/', views.fancreo, name="fancreo"),
	path('signup/', views.signup, name="signup"),
]