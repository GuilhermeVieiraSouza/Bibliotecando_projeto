from django.urls import path

from . import views

urlpatterns = [
    path('descubra/', views.descubra, name='descubra'),
    path('meusLivros/', views.MeusLivros, name='meusLivros'),
    path('detalhesLivro/<int:id>/', views.detalhesLivro, name='detalhesLivro'),
    path('registro/', views.registro, name='registro'),
     path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),

]