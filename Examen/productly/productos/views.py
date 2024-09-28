from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  
from .models import Producto, Categoria

def index(request):
    # Obtener todos los productos y categorías
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    
    # Si el método de la solicitud es POST, significa que se envió el formulario
    if request.method == 'POST':
        nombre = request.POST['nombre']  # Capturar el nombre del producto
        stock = request.POST['stock']  # Capturar el stock
        puntaje = request.POST['puntaje']  # Capturar el puntaje
        categoria_id = request.POST['categoria']  # Capturar la categoría seleccionada

        # Obtener la instancia de la categoría seleccionada
        categoria = Categoria.objects.get(id=categoria_id)

        # Crear un nuevo producto con los datos recibidos
        nuevo_producto = Producto(
            nombre=nombre,
            stock=stock,
            puntaje=puntaje,
            categoria=categoria
        )

        # Guardar el nuevo producto en la base de datos
        nuevo_producto.save()
        
        # Redirigir a la vista de inicio para evitar el reenvío del formulario
        return redirect('index')  # Cambia a 'index' para redirigir a la vista de inicio

    # Renderizar la plantilla index.html, pasando los productos y las categorías
    return render(request, 'index.html', {'productos': productos, 'categorias': categorias}) 

def categoria_view(request):
    categorias = Categoria.objects.all()
    
    if request.method == 'POST':
        nombre_categoria = request.POST.get('nombre')
        if nombre_categoria:
            nueva_categoria = Categoria(nombre=nombre_categoria)
            nueva_categoria.save()
            return redirect('categoria')  # Redirige a la misma vista después de agregar
    
    return render(request, 'categoria.html', {'categorias': categorias})

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('categoria')  # Redirige a la vista de categorías

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        nombre_categoria = request.POST.get('nombre')
        if nombre_categoria:
            categoria.nombre = nombre_categoria
            categoria.save()
            return redirect('categoria')  # Redirige a la vista de categorías

    return render(request, 'editar_categoria.html', {'categoria': categoria})
def productos_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        stock = request.POST.get('stock')
        puntaje = request.POST.get('puntaje')
        categoria_id = request.POST.get('categoria')
        
        # Lógica para agregar el producto
        nueva_categoria = Categoria.objects.get(id=categoria_id)
        Producto.objects.create(nombre=nombre, stock=stock, puntaje=puntaje, categoria=nueva_categoria)
        return redirect('productos')  # Redirigir a la misma vista después de agregar

    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'categorias': categorias, 'productos': productos})

def modificar_producto_view(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        # Actualizar el producto con los datos del formulario
        producto.nombre = request.POST['nombre']
        producto.stock = request.POST['stock']
        producto.puntaje = request.POST['puntaje']
        producto.categoria = Categoria.objects.get(id=request.POST['categoria'])
        producto.save()
        
        return redirect('index')  # Redirigir a la vista de inicio después de modificar

    return render(request, 'modificar_producto.html', {'producto': producto, 'categorias': categorias})

# Añade la función eliminar_producto
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('index')  # Redirige a la vista de inicio después de eliminar

def agregar_producto_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        stock = request.POST.get('stock')
        puntaje = request.POST.get('puntaje')
        categoria_id = request.POST.get('categoria')

        # Verificar si hay categorías antes de agregar el producto
        if not Categoria.objects.exists():
            messages.error(request, 'Debe agregar al menos una categoría antes de agregar un producto.')
            return render(request, 'agregar_producto.html')  # Vuelve a cargar el formulario con el mensaje

        # Si hay categorías, continúa con la creación del producto
        categoria = Categoria.objects.get(id=categoria_id)
        nuevo_producto = Producto(nombre=nombre, stock=stock, puntaje=puntaje, categoria=categoria)
        nuevo_producto.save()
        messages.success(request, 'Producto agregado exitosamente.')
        return redirect('index')

    else:
        categorias = Categoria.objects.all()  # Obtiene las categorías para el formulario
        return render(request, 'agregar_producto.html', {'categorias': categorias})
    
def detalle_producto_view(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def productos_list_view(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'productos/productos_list.html', {'productos': productos})

def examen(request):
    return render(request, 'examen.html')