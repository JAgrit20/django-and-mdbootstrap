from django.shortcuts import render

#just a simple function which will render home.html when called

def home(request):

 return render(request,'pages/home.html')