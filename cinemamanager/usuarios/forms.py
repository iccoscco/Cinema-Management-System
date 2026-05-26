from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario
from validators import validar_edad, validar_password


class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Mínimo 8 caracteres'}),
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repite tu contraseña'}),
    )
    edad = forms.IntegerField(
        label='Edad',
        widget=forms.NumberInput(attrs={'placeholder': '13 - 100'}),
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'edad', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
        }

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad is None:
            raise forms.ValidationError("La edad es obligatoria.")
        try:
            validar_edad(int(edad))
        except (TypeError, ValueError) as e:
            raise forms.ValidationError(str(e))
        return edad

    def clean_password1(self):
        password = self.cleaned_data.get('password1', '')
        try:
            validar_password(password)
        except (TypeError, ValueError) as e:
            raise forms.ValidationError(str(e))
        return password

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('password1')
        p2 = cleaned.get('password2')
        if p1 and p2 and p1 != p2:
            self.add_error('password2', 'Las contraseñas no coinciden.')
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Usuario'}),
        label='Usuario',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        label='Contraseña',
    )
