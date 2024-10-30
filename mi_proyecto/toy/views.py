from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Usuario
from .forms import ProductoForm, UsuarioForm

# Vista para listar todos los productos
def lista_productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos de la base de datos
    return render(request, 'templates/lista_productos.html', {'productos': productos})

# Vista para crear un nuevo producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)  # Crear formulario 
        if form.is_valid():  # Validar el formulario 
            form.save()  # Guardar
            return redirect('lista_productos')  # Redirigir a la lista de productos
    else:
        form = ProductoForm()  # Mostrar formulario vacío 
    return render(request, 'templates/crear_producto.html', {'form': form})

# Vista para editar un producto existente
def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)  # Obtener el producto o devolver error 404
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)  # Crear formulario con datos del producto 
        if form.is_valid():  # Validar el formulario
            form.save()  # Guardar 
            return redirect('lista_productos')  # Redirigir a la lista de productos
    else:
        form = ProductoForm(instance=producto)  # Mostrar formulario con los datos del producto
    return render(request, 'templates/editar_producto.html', {'form': form})

# Vista para eliminar un producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)  # Obtener el producto o devolver error 404
    if request.method == 'POST':
        producto.delete()  # Eliminar el producto
        return redirect('lista_productos')  # Redirigir a la lista de productos
    return render(request, 'templates/eliminar_producto.html', {'producto': producto})


###### Vistas para Usuario

# Vista para listar todos los usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()  # Obtener todos los usuarios de la base de datos
    return render(request, 'templates/lista_usuarios.html', {'usuarios': usuarios})

# Vista para crear un nuevo usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)  # Crear formulario 
        if form.is_valid():  # Validar el formulario 
            user = form.save()  # Guardar el nuevo usuario
            return redirect('lista_usuarios')  # Redirigir a la lista de usuarios
    else:
        form = UsuarioForm()  # Mostrar formulario vacío 
    return render(request, 'templates/crear_usuario.html', {'form': form})

# Vista para editar un usuario existente
def actualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)  # Obtener el usuario o devolver error 404
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)  # Crear formulario con datos del usuario existente
        if form.is_valid():  # Validar el formulario
            form.save()  # Guardar 
            return redirect('lista_usuarios')  # Redirigir a la lista de usuarios
    else:
        form = UsuarioForm(instance=usuario)  # Mostrar formulario con los datos del usuario
    return render(request, 'templates/editar_usuario.html', {'form': form})

# Vista para eliminar un usuario
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)  # Obtener el usuario o devolver error 404
    if request.method == 'POST':
        usuario.user.delete()  # Eliminar el usuario 
        usuario.delete()  # Eliminar el usuario de la base de datos
        return redirect('lista_usuarios')  # Redirigir a la lista de usuarios
    return render(request, 'templates/eliminar_usuario.html', {'usuario': usuario})