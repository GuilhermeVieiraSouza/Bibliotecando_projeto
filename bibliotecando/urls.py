from django.urls import path

from . import views

urlpatterns = [
    path('descubra/', views.descubra, name='descubra'),
    path('meusLivros/', views.MeusLivros, name='meusLivros'),
]