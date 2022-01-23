from django.urls import path
from mainpage import views

urlpatterns = [
    path('', views.mainpage, name='index'),
    path('about/', views.about, name='about'),
]