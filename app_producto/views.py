from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Producto
from .forms import ProductoForm


# Create your views here.
def index(request):
  return render(request, 'productos/index.html', {
    'productos': Producto.objects.all()
  })


def view_producto(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = ProductoForm(request.POST)
    if form.is_valid():
      new_nombre_producto = form.cleaned_data['nombre_producto']
      new_descripcion = form.cleaned_data['descripcion']
      new_precio = form.cleaned_data['precio']
      new_categoria = form.cleaned_data['categoria']
      new_disponibilidad = form.cleaned_data['disponibilidad']
      new_id_ingrediente = form.cleaned_data['id_ingrediente']

      new_producto = Producto(
        nombre_producto=new_nombre_producto,
        descripcion=new_descripcion,
        precio=new_precio,
        categoria=new_categoria,
        disponibilidad=new_disponibilidad,
        id_ingrediente=new_id_ingrediente
      )
      new_producto.save()
      return render(request, 'productos/add.html', {
        'form': ProductoForm(),
        'success': True
      })
  else:
    form = ProductoForm()
  return render(request, 'productos/add.html', {
    'form': ProductoForm()
  })


def edit(request, id):
  if request.method == 'POST':
    producto = Producto.objects.get(pk=id)
    form = ProductoForm(request.POST, instance=producto)
    if form.is_valid():
      form.save()
      return render(request, 'productos/edit.html', {
        'form': form,
        'success': True
      })
  else:
    producto = Producto.objects.get(pk=id)
    form = ProductoForm(instance=producto)
  return render(request, 'productos/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    producto = Producto.objects.get(pk=id)
    producto.delete()
  return HttpResponseRedirect(reverse('index'))