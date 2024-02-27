from django import forms

from world_of_speed_app.cars.models import Car
from world_of_speed_app.profiles.models import Profile


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ["owner"]
        owner = Profile.objects.latest('id').id
        widgets = {
            "type": forms.Select(),
            "model": forms.TextInput(),
            "year": forms.NumberInput(),
            "image_url": forms.URLInput(),
            "price": forms.NumberInput(),
        }


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ["owner"]
        widgets = {
            "type": forms.Select(),
            "model": forms.TextInput(),
            "year": forms.NumberInput(),
            "image_url": forms.URLInput(),
            "price": forms.NumberInput(),
        }


class DeleteCarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeleteCarForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

    class Meta:
        model = Car
        exclude = ["owner"]
        widgets = {
            "type": forms.Select(attrs={'disabled': True, 'readonly': 'readonly'}),
            "model": forms.TextInput(attrs={'disabled': True, 'readonly': 'readonly'}),
            "year": forms.NumberInput(attrs={'disabled': True, 'readonly': 'readonly'}),
            "image_url": forms.URLInput(attrs={'disabled': True, 'readonly': 'readonly'}),
            "price": forms.NumberInput(attrs={'disabled': True, 'readonly': 'readonly'}),
        }
