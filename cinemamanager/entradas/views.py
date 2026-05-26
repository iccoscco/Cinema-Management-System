from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from peliculas.models import Pelicula
from .models import Funcion, Compra
from .forms import CompraForm, FuncionForm
from peliculas.views import solo_admin


@login_required
def comprar(request, pelicula_pk):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_pk)
    if request.method == 'POST':
        form = CompraForm(pelicula=pelicula, data=request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            cantidad = form.cleaned_data['cantidad']
            total = funcion.precio * cantidad
            compra = Compra.objects.create(
                usuario=request.user,
                funcion=funcion,
                cantidad=cantidad,
                total=total,
            )
            messages.success(request, f'¡Compra exitosa! {cantidad} entrada(s) para "{pelicula.titulo}". Total: S/ {total}')
            return redirect('historial')
    else:
        form = CompraForm(pelicula=pelicula)

    return render(request, 'entradas/comprar.html', {'form': form, 'pelicula': pelicula})


@login_required
def historial(request):
    compras = Compra.objects.filter(usuario=request.user).select_related('funcion__pelicula')
    return render(request, 'entradas/historial.html', {'compras': compras})


@solo_admin
def gestionar_funciones(request):
    funciones = Funcion.objects.all().select_related('pelicula')
    return render(request, 'entradas/gestionar_funciones.html', {'funciones': funciones})


@solo_admin
def crear_funcion(request):
    if request.method == 'POST':
        form = FuncionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Función creada correctamente.')
            return redirect('gestionar_funciones')
    else:
        form = FuncionForm()
    return render(request, 'entradas/form_funcion.html', {'form': form, 'titulo': 'Crear Función'})


@solo_admin
def eliminar_funcion(request, pk):
    funcion = get_object_or_404(Funcion, pk=pk)
    if request.method == 'POST':
        funcion.delete()
        messages.success(request, 'Función eliminada.')
        return redirect('gestionar_funciones')
    return render(request, 'entradas/confirmar_eliminar_funcion.html', {'funcion': funcion})
