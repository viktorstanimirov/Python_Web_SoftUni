from django import forms

from world_of_speed_app.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "email", "age", "password")

        widgets = {
            "username": forms.TextInput(),

            "email": forms.EmailInput(),
            "age": forms.NumberInput(),

            "password": forms.PasswordInput(),

        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        widgets = {
            "username": forms.TextInput(),

            "email": forms.EmailInput(),
            "age": forms.NumberInput(),
        }


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Profile
        fields = ()
