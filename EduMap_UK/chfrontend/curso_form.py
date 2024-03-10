from django import forms
from .models import Curso

class CursoCreateForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'instituicao', 'duracao', 'tipo_certificado', 'custo_de_vida', 'avaliacao_final']
