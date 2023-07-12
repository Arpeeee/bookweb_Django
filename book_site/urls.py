from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name="testpage"),
    path('html/', views.view_home, name="html")
]