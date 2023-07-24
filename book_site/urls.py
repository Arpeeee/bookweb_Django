from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hello_world, name="testpage"),
    # path("test", views.Testreview, name="testreview"),
    path('html/', views.view_home, name="html"),
    path('api/review', views.api_Review),
    path('api/login', views.login)
    # path('api/', include("api.urls"))
]