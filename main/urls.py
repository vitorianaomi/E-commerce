
from django.contrib import admin
from django.urls import path
from venda.views import index,produto_criar, produto_listar, produto_editar, produto_remover, produto_detalhar
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('produto/criar/', produto_criar, name = 'produto_criar'),
    path('produto/editar/<int:id>/', produto_editar, name = 'produto_editar'),
    path('produto/remover/<int:id>/', produto_remover, name = 'produto_remover'),
    path('produto/listar/', produto_listar, name = 'produto_listar'),
    path('produto/<int:id_produto>',produto_detalhar,name='produto_detalhar'),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
