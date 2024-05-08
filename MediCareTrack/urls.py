from django.contrib import admin
from django.urls import path, include
from medassistente import urls as medassistente_urls  # Importe as URLs do app farmacia
from farmacia import urls as farmacia_urls  # Importe as URLs do app farmacia
#from accounts import urls as acconts_urls  # Importe as URLs de outro_app

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('assistente/', include(medassistente_urls)),  # Inclua as URLs do app farmacia
    path('farmacia/', include(farmacia_urls)),  # Inclua as URLs do app farmacia
    #path('accounts/', include(acconts_urls)),  # Inclua as URLs de outro_app
    path('accounts/', include('allauth.urls'))
]