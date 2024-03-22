from django.urls import reverse_lazy
from django.views import generic as view

from MyPlant_App.plants.models import Plant
from MyPlant_App.profiles.forms import CreateProfileForm, DeleteProfileForm
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


class ProfileDetailsView(view.TemplateView):
    template_name = "profiles/profile-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = get_profile()
        plants = Plant.objects.all()
        context["profile"] = profile
        context["plants"] = plants
        return context


class ProfileEditView(view.UpdateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = "profiles/edit-profile.html"

    def get_success_url(self):
        return reverse_lazy("details profile", kwargs={"pk": self.object.id})


class ProfileDeleteView(view.DeleteView):
    model = Profile
    form_class = DeleteProfileForm
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("index")
