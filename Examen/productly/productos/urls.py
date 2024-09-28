# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/', views.categoria_view, name='categoria'),
    path('eliminar_categoria/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('editar_categoria/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('productos/', views.productos_view, name='productos'),
    path('modificar_producto/<int:producto_id>/', views.modificar_producto_view, name='modificar_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('agregar_producto/', views.agregar_producto_view, name='agregar_producto'),
    path('detalle_producto/<int:producto_id>/', views.detalle_producto_view, name='detalle_producto'),  
    path('examen/', views.examen, name='examen'), 
]
