from django.urls import path
from .views import hello_world,hi_world

urlpatterns = [
    path('',hello_world,name="hello-world"),
    path('hi/',hi_world,name="hi-world")
]