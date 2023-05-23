from django import forms
from .models import quiz_model

class quiz_form(forms.ModelForm):
    class Meta:
        model = quiz_model
        fields = ['question', 'option1','option2','option3','option4', 'right_answer_index', 'start_date', 'end_date']
