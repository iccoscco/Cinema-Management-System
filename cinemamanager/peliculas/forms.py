from django import forms
from .models import Pelicula, Comentario
from validators import validar_duracion, validar_rating, validar_comentario


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'descripcion', 'duracion', 'genero', 'imagen', 'anio', 'destacada']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título de la película'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Sinopsis...'}),
            'duracion': forms.NumberInput(attrs={'placeholder': '60 - 300 minutos'}),
            'anio': forms.NumberInput(attrs={'placeholder': 'Año de estreno'}),
        }

    def clean_duracion(self):
        duracion = self.cleaned_data.get('duracion')
        if duracion is None:
            raise forms.ValidationError("La duración es obligatoria.")
        try:
            validar_duracion(int(duracion))
        except (TypeError, ValueError) as e:
            raise forms.ValidationError(str(e))
        return duracion


class ComentarioForm(forms.ModelForm):
    RATING_CHOICES = [(i, '★' * i) for i in range(1, 6)]
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect,
        label='Calificación',
    )

    class Meta:
        model = Comentario
        fields = ['texto', 'rating']
        widgets = {
            'texto': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Escribe tu comentario (1-500 caracteres)...',
                'maxlength': 500,
            }),
        }
        labels = {'texto': 'Comentario'}

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        try:
            validar_rating(int(rating))
        except (TypeError, ValueError) as e:
            raise forms.ValidationError(str(e))
        return int(rating)

    def clean_texto(self):
        texto = self.cleaned_data.get('texto', '')
        try:
            validar_comentario(texto)
        except (TypeError, ValueError) as e:
            raise forms.ValidationError(str(e))
        return texto


class BusquedaForm(forms.Form):
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Buscar película...'}),
        label='',
    )
