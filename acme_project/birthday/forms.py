from typing import Final, Set

from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Birthday, Congratulation


BEATLES: Final[Set] = {
    'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'
}


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(
                attrs={'type': 'date'},
                format="%Y-%m-%d")
        }

    def clean_first_name(self) -> str:
        first_name: str = self.cleaned_data['first_name']
        return first_name.split()[0]
    
    def clean(self) -> None:
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        if f'{first_name} {last_name}' in BEATLES:
            send_mail(
                subject='Another Beatles member',
                message=f'{first_name} {last_name} пытался опубликовать запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=False,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )


class CongratulationForm(forms.ModelForm):

    class Meta:
        model = Congratulation
        fields = ('text', )