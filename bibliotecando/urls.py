from django.urls import path

from . import views

app_name = 'bibliotecando'

urlpatterns = [
    path('', views.descubra, name='descubra'),
    path('meusLivros/', views.MeusLivros, name='meusLivros'),
    path('detalhesLivro/<int:id>/', views.detalhesLivro, name='detalhesLivro'),
    path('profile/', views.profile, name='profile'),
    #urls de login
    path('registro/', views.register, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]