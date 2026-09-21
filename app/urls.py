from django.urls import include, path

urlpatterns = [
    # ... otras rutas ...
    path('usuarios/', include('usuarios.urls')),  # <-- Agrega .urls
]