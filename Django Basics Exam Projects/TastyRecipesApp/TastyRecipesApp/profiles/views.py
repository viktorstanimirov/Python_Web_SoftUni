from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic as view

from TastyRecipesApp.profiles.forms import CreateProfileForm, UpdateProfileForm, DeleteProfileForm
from TastyRecipesApp.profiles.models import Profile


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


class DetailsProfileView(view.DetailView):
    model = Profile
    template_name = "profiles/details-profile.html"
    context_object_name = "profile"

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        profile = queryset.first()
        if profile is None:
            raise Http404("No Profile exists.")
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = context['profile']
        context['recipes'] = profile.recipes.all()
        context['recipes_count'] = profile.recipes.count()

        return context


class ProfileEditView(view.UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = "profiles/edit-profile.html"

    def get_success_url(self):
        return reverse_lazy("details-profile", kwargs={"pk": self.object.id})


class ProfileDeleteView(view.DeleteView):
    model = Profile
    form_class = DeleteProfileForm
    template_name = "profiles/delete-profile.html"
    success_url = reverse_lazy("home-page")