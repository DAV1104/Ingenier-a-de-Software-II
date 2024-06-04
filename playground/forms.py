from django import forms
from .models import Usuario

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    rol = forms.ChoiceField(choices=[('profesor', 'Profesor'), ('estudiante', 'Estudiante')], widget=forms.Select(attrs={'class': 'custom-select'}))

    class Meta:
        model = Usuario
        fields = ['nombre_completo', 'nombre_usuario', 'email', 'password', 'confirm_password', 'rol']

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and confirm password does not match"
            )

class UserLoginForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        nombre_usuario = cleaned_data.get("nombre_usuario")
        password = cleaned_data.get("password")

        try:
            user = Usuario.objects.get(nombre_usuario=nombre_usuario)
        except Usuario.DoesNotExist:
            raise forms.ValidationError("Invalid username or password.")

        if not user.check_password(password):
            raise forms.ValidationError("Invalid username or password.")

        cleaned_data["user"] = user
        return cleaned_data