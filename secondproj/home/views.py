from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    context={
        "variable": "i am sik",
        "variable2": "i can only dev"
    }
    return render(request,   'index.html', context)

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is server page")

def contact(request):
    return HttpResponse("this is contact page")