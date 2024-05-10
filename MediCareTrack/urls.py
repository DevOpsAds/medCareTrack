from django.contrib import admin
from django.urls import path, include
from medassistente import urls as medassistente_urls  # Importe as URLs do app farmacia
from farmacia import urls as farmacia_urls  # Importe as URLs do app farmacia
from django.contrib.auth.decorators import login_required

from accounts.views import salvar_usuario_vinculado,UserProfileView,test_usuario_vinculado,criar_usuario_vinculado
urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('assistente/', include(medassistente_urls)),  # Inclua as URLs do app farmacia
    path('farmacia/', include(farmacia_urls)),  # Inclua as URLs do app farmacia
    #path('accounts/', include(acconts_urls)),  # Inclua as URLs de outro_app
    path('accounts/', include('allauth.urls')),
    path('criar_membro_equipe/', criar_usuario_vinculado, name='criar_membro_equipe'),
    path('salvar_membro_equipe/', salvar_usuario_vinculado, name='salver_membro_equipe'),
    path('teste-usuario/', test_usuario_vinculado, name='test_usuario_vinculado'),
        # Corrija a inclusão da view diretamente
    path('accounts/profile/', login_required(UserProfileView.as_view()), name='profile'),
]