from django.urls import path

from uimaster import views

#just we are calling from home function from views.py

urlpatterns = [

  path('home',views.home, name='home'),

]