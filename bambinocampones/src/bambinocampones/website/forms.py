from django.forms import ModelForm
from .models import Depoimento


class DepoimentoForm(ModelForm):
    class Meta:
        model = Depoimento
