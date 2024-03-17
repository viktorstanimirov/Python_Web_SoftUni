from django import forms

from MyPlant_App.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class CreateProfileForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = ("profile_picture",)
