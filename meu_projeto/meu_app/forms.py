from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['fornecedor', 'avaliacao', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'avaliacao': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
