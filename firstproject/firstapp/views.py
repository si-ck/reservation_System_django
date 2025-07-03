from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
def hell_world(request):
    return HttpResponse("Hello, world!")


class HelloSik(View):
    def get(self, request):
        return HttpResponse("Hello Sik!")