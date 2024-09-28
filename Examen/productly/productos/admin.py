from django.contrib import admin
from .models import Categoria, Producto
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)

class CategoriaAdmin(admin.ModelAdmin):
    list_display=('id', 'nombre')
class ProductoAdmin(admin.ModelAdmin):
    exclude=('creado_en',)
    list_display=('id','nombre','stock','creado_en')