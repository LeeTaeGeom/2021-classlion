from django.shortcuts import render

# Create your views here.

def showmain(request):
    return render(request, 'main/cover.html')

def showintro(request):
    return render(request, 'main/intro.html')

def showhobby(request):
    return render(request, 'main/hobby.html')

def shownetflix(request):
    return render(request, 'main/netflix.html')

def showfood(request):
    return render(request, 'main/food.html')
    