from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views  # Importe as views do app accounts
from farmacia import views as farmacia_views  # Importe as views do app farmacia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', accounts_views.profile, name="profile"),  # Rota para o perfil do usuário
    path('farmacia/', farmacia_views.entrada_estoque, name="entrada_estoque"),  # Rota para a entrada de estoque na farmácia
]

from farmacia import urls as farmacia_urls  # Importe as URLs do app farmacia
from outro_app import urls as outro_app_urls  # Importe as URLs de outro_app

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('farmacia/', include(farmacia_urls)),  # Inclua as URLs do app farmacia
    path('outro_app/', include(outro_app_urls)),  # Inclua as URLs de outro_app
]