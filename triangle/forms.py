from django import forms
from django.core.exceptions import ValidationError

from .models import Person


class PersonForm(forms.ModelForm):
    model = Person
    field = ["first_name", "last_name", "email"]

    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email"]


class TriangleForm(forms.Form):
    cathetus1 = forms.IntegerField(required=True)
    cathetus2 = forms.IntegerField(required=True)

    def get_cathetus1(self):
        cathetus1 = self.cleaned_data.get('cathetus1')
        if cathetus1 <= 0:
            raise ValidationError("Catheters must be greater than 0")
        return cathetus1

    def get_cathetus2(self):
        cathetus2 = self.cleaned_data.get('cathetus2')
        if cathetus2 <= 0:
            raise ValidationError("Catheters must be greater than 0")
        return cathetus2
