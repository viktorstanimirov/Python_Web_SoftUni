from django.urls import reverse_lazy
from django.views import generic as view
from MyPlant_App.profiles.forms import CreateProfileForm
from MyPlant_App.profiles.models import Profile


def get_profile():
    try:
        profile = Profile.objects.first()
        return profile
    except Exception:
        return None


class CreateProfileView(view.CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = "profiles/create-profile.html"
    success_url = reverse_lazy("catalogue")
