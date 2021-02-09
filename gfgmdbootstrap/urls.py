from django.contrib import admin

from django.urls import path

from uimaster import views

urlpatterns = [

  path('admin/', admin.site.urls),

#here we have not add anything in the inverted commas so that it will open as the default page

  path('',views.home,name='home'),

]