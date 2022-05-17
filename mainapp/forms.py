from django.forms import ModelForm, Textarea, TextInput, CheckboxInput

from .models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['full_name', 'location', 'phone', 'email', 'question', 'agree_privacy']

        widgets = {
            'full_name': TextInput(attrs={
                'id': 'name',
                'class': 'form__input',
                'name': 'name',
                'type': 'text'
            }),
            'location': TextInput(attrs={
                'id': 'residence',
                'class': 'form__input',
                'name': 'residence',
                'type': 'text'
            }),
            'phone': TextInput(attrs={
                'id': 'phone',
                'class': 'form__input',
                'name': 'phone',
                'type': 'tel'
            }),
            'email': TextInput(attrs={
                'id': 'email',
                'class': 'form__input',
                'name': 'email',
                'type': 'email'
            }),
            'question': Textarea(attrs={
                'id': 'textarea',
                'class': 'form__textarea',
                'name': 'textarea'
            }),
            'agree_privacy': CheckboxInput(attrs={
                'id': 'agree',
                'class': 'form__checkbox',
                'name': 'agree',
                'type': 'checkbox',
                'required': ''
            }),
        }
