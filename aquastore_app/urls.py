from django.urls import path

from . import views

app_name = 'aquastore_app'

urlpatterns = [
    path(r'', views.lista_aguas, name='lista_aguas'),
    path(r'cat/<slug:slug_da_categoria>/', views.lista_aguas, name='lista_aguas_por_categoria'),
    path(r'produto/(<int:id>)', views.exibe_agua, name='exibe_agua'),
    path(r'sobre.html', views.sobre, name='sobre'),
    path(r'cadastro.html', views.novo, name='cadastro'),
    path(r'admin.html', views.admin, name='admin'),
    path(r'<int:id>/update', views.atualiza, name='atualiza'),
    path(r'<int:id>/delete', views.deleta, name='deleta'),
    path(r'register.html', views.register, name='register'),
    path(r'logout', views.logout_user, name='logout_user'),
]

