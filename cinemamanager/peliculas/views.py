from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Pelicula, Genero, Comentario
from .forms import PeliculaForm, ComentarioForm, BusquedaForm


def catalogo(request):
    form = BusquedaForm(request.GET)
    peliculas = Pelicula.objects.all()
    generos = Genero.objects.all()
    genero_sel = request.GET.get('genero')
    query = ''

    if form.is_valid():
        query = form.cleaned_data.get('q', '')
        if query:
            peliculas = peliculas.filter(
                Q(titulo__icontains=query) | Q(descripcion__icontains=query)
            )

    if genero_sel:
        peliculas = peliculas.filter(genero__id=genero_sel)

    destacadas = Pelicula.objects.filter(destacada=True)[:3]
    return render(request, 'peliculas/catalogo.html', {
        'peliculas': peliculas,
        'generos': generos,
        'form': form,
        'query': query,
        'genero_sel': genero_sel,
        'destacadas': destacadas,
    })


def detalle(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    comentarios = pelicula.comentarios.all().order_by('-fecha')
    ya_comento = False
    form = None

    if request.user.is_authenticated:
        ya_comento = comentarios.filter(usuario=request.user).exists()
        if not ya_comento:
            form = ComentarioForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, 'Debes iniciar sesión para comentar.')
            return redirect('login')
        if ya_comento:
            messages.warning(request, 'Ya dejaste un comentario en esta película.')
            return redirect('detalle', pk=pk)
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.pelicula = pelicula
            comentario.usuario = request.user
            comentario.save()
            messages.success(request, '¡Comentario publicado!')
            return redirect('detalle', pk=pk)

    return render(request, 'peliculas/detalle.html', {
        'pelicula': pelicula,
        'comentarios': comentarios,
        'form': form,
        'ya_comento': ya_comento,
    })


@login_required
def toggle_favorito(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    user = request.user
    if pelicula in user.favoritos.all():
        user.favoritos.remove(pelicula)
        messages.info(request, f'"{pelicula.titulo}" eliminado de favoritos.')
    else:
        user.favoritos.add(pelicula)
        messages.success(request, f'"{pelicula.titulo}" agregado a favoritos.')
    return redirect('detalle', pk=pk)


# ─── Admin views ───

def solo_admin(view_func):
    from functools import wraps
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.rol != 'admin' and not request.user.is_superuser:
            messages.error(request, 'No tienes permisos para acceder a esta sección.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper


@solo_admin
def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Película agregada correctamente.')
            return redirect('home')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/form_pelicula.html', {'form': form, 'titulo': 'Agregar Película'})


@solo_admin
def editar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            messages.success(request, 'Película actualizada.')
            return redirect('detalle', pk=pk)
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'peliculas/form_pelicula.html', {'form': form, 'titulo': 'Editar Película'})


@solo_admin
def eliminar_pelicula(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        titulo = pelicula.titulo
        pelicula.delete()
        messages.success(request, f'"{titulo}" eliminada.')
        return redirect('home')
    return render(request, 'peliculas/confirmar_eliminar.html', {'pelicula': pelicula})
