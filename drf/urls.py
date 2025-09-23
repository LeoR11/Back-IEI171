from django.contrib import admin
from django.urls import path, include
from biblioteca import views
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.pagina_inicio, name='home'),
  path('biblioteca/', include('biblioteca.urls')),
 
]