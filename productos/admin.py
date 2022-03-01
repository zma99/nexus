from django.contrib import admin
from .models import Producto, Cliente

#admin.site.register(Producto)
#admin.site.register(Cliente)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'categoria', 'stock', 'precio')
    ordering = ('codigo',)
    search_fields = ('codigo', 'nombre')
    list_display_links = ('nombre',)
    list_filter = ('categoria',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'apellido', 'nombre', 'condicion_iva')
    ordering = ('id',)
    search_fields = ('id', 'apellido', 'nombre')
    list_display_links = ('id',)
    list_filter = ('condicion_iva',)

