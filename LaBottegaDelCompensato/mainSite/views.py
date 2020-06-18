from django.shortcuts import render

def home(request):
    return render(request, 'mainSite/home.html')

# Create your views here.
