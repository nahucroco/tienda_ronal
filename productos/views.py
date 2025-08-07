from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

def home(request):
    productos = Producto.objects.filter(disponible=True)
    return render(request, 'productos/home.html', {'productos': productos})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("❌ Formulario no válido:")
            print(form.errors)  # Mostrá los errores en consola para depurar
    else:
        form = ProductoForm()
    return render(request, 'productos/formulario.html', {'form': form})

