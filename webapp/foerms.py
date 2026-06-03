from django import forms
from webapp.models import Task, STATUS_CHOICES

class TaskForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    detailed_description = forms.CharField(
        widget=forms.Textarea,
        label='Подробное описание',
        required=False
    )
    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Статус')
    due_date = forms.DateField(
        required=False,
        label='Дата выполнения',
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )