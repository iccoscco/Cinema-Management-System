from django import forms
from .models import Compra, Funcion
from validators import validar_cantidad_entradas, validar_anio_funcion


class CompraForm(forms.Form):
    funcion = forms.ModelChoiceField(
        queryset=Funcion.objects.none(),
        label='Función',
        widget=forms.Select,
    )
    cantidad = forms.IntegerField(
        label='Cantidad de entradas',
        min_value=1, max_value=10,
        widget=forms.NumberInput(attrs={'placeholder': '1 - 10', 'min': 1, 'max': 10}),
    )

    def __init__(self, pelicula=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if pelicula:
            self.fields['funcion'].queryset = Funcion.objects.filter(
                pelicula=pelicula
            ).order_by('fecha_hora')

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is None:
            raise forms.ValidationError("La cantidad es obligatoria.")
        try:
            validar_cantidad_entradas(int(cantidad))
        except (TypeError, ValueError) as e:
            raise forms.ValidationError(str(e))
        return cantidad

    def clean(self):
        cleaned = super().clean()
        funcion = cleaned.get('funcion')
        cantidad = cleaned.get('cantidad')
        if funcion and cantidad:
            if cantidad > funcion.asientos_disponibles:
                raise forms.ValidationError(
                    f"Solo quedan {funcion.asientos_disponibles} asientos disponibles."
                )
        return cleaned


class FuncionForm(forms.ModelForm):
    def clean_fecha_hora(self):
        fecha_hora = self.cleaned_data.get('fecha_hora')
        if fecha_hora is None:
            raise forms.ValidationError("La fecha y hora son obligatorias.")
        try:
            validar_anio_funcion(int(fecha_hora.year))
        except (TypeError, ValueError) as e:
            raise forms.ValidationError(str(e))
        return fecha_hora

    class Meta:
        model = Funcion
        fields = ['pelicula', 'fecha_hora', 'sala', 'asientos_totales', 'precio']
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'sala': forms.TextInput(attrs={'placeholder': 'Ej: Sala 1'}),
            'precio': forms.NumberInput(attrs={'placeholder': 'Precio por entrada'}),
        }
