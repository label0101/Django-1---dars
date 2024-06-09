from django.shortcuts import render
from django.http import HttpResponse




def hello_world(request):
    return render(request=request, template_name="index.html")

def hi_world(request):
    return render(request=request, template_name="hi.html")
