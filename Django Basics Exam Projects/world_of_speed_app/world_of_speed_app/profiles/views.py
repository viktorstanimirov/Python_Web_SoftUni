from django.db.models import Sum
from django.shortcuts import render, redirect

from world_of_speed_app.cars.models import Car
from world_of_speed_app.profiles.forms import CreateProfileForm, EditProfileForm
from world_of_speed_app.profiles.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    return render(request, "profiles/profile-create.html", {'form': form})


# ''' TODO: Check the profile full_name'''
def profile_details(request):
    profile = Profile.objects.first()
    full_name = profile.full_name
    total_sum = Car.objects \
                    .filter(owner=profile, owner__isnull=False) \
                    .aggregate(total_price=Sum('price'))['total_price'] or 0

    context = {
        "profile": profile,
        "total_sum": total_sum

    }
    return render(request, "profiles/profile-details.html", context=context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        "profile": profile,
        "form": form
    }
    return render(request, "profiles/profile-edit.html", context=context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        return redirect('index')
    return render(request, "profiles/profile-delete.html")

