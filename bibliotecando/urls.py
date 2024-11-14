from django.urls import path

from . import views

urlpatterns = [
    path('', views.descubra, name='descubra'),
    path('meusLivros/', views.MeusLivros, name='meusLivros'),
    path('detalhesLivro/<int:id>/', views.detalhesLivro, name='detalhesLivro'),
    path('registro/', views.register, name='registro'),
     path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),

]