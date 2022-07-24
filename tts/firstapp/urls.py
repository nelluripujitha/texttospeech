from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('ss',views.some,name='some')
]
