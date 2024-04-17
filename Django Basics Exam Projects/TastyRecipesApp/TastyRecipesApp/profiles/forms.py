from django import forms

from TastyRecipesApp.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class CreateProfileForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = ("bio",)


class UpdateProfileForm(ProfileBaseForm):
    pass


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []
