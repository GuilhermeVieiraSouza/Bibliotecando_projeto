from django.urls import path

from . import views

urlpatterns = [
    path('descubra/', views.descubra, name='descubra'),
    path('meusLivros/', views.MeusLivros, name='meusLivros'),
    path('detalhesLivro/<int:id>/', views.detalhesLivro, name='detalhesLivro'),
    path('registro/', views.login, name='registro')
]