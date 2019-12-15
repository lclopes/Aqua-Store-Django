from django.urls import path

from autenticacao.views import login_user, submit_login, logout_user
app_name = 'autenticacao'

urlpatterns = [
    path('login', login_user, name='login_user'),
    path('submit', submit_login, name='submit_login'),
    path('logout', logout_user, name='logout_user'),
]