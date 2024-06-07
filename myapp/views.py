from django.shortcuts import render
from django.http import HttpResponse




def hello_world(request):
    return HttpResponse("<h1>Assalomu alaykum Sifat</h1>")
