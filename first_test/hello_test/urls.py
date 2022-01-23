from django.urls import path
from hello_test import views

urlpatterns=[path('',views.hello_test, name='hello_test')]

