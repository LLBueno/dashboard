from django import forms
from .models import Feriado


class DateInput(forms.DateInput):
    input_type = 'date'


class FeriadoForm(forms.ModelForm):

    class Meta:
        model = Feriado
        fields = [
            'nome',
            'data',
        ]
        localized_fields = ['data']
        widgets = {
            'data': DateInput(),
        }
