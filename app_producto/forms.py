from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [ 'nombre_producto', 'descripcion', 'precio', 'categoria', 'disponibilidad', 'id_ingrediente']
        labels = {
            'nombre_producto': 'Nombre Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'categoria': 'Categoría',
            'disponibilidad': 'Disponibilidad',
            'id_ingrediente': 'ID Ingrediente'
        }
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'disponibilidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'id_ingrediente': forms.NumberInput(attrs={'class': 'form-control'}),
        }