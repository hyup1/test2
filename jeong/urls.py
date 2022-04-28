from django.urls import path

from jeong.views import hello

urlpatterns = [
    path('jeong/', hello, name='hello')
]