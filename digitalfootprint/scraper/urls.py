from django.urls import path
from scraper import views

urlpatterns=[path('',views.scraper, name='scraper')]