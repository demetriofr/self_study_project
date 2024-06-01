from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'question_text': forms.Textarea(attrs={'class': 'wide-text'}),
            'description': forms.Textarea(attrs={'class': 'wide-text'}),
            'topic': forms.Textarea(attrs={'class': 'wide-text'}),
            'explanation': forms.Textarea(attrs={'class': 'wide-textarea'}),
            'option_a': forms.Textarea(attrs={'class': 'wide-text'}),
            'option_b': forms.Textarea(attrs={'class': 'wide-text'}),
            'option_c': forms.Textarea(attrs={'class': 'wide-text'}),
            'option_d': forms.Textarea(attrs={'class': 'wide-text'}),
        }

    class Media:
        css = {
            'all': ('knowledge_testing/admin.css',)
        }
