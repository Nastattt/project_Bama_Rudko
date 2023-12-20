from django import forms

from app.models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'