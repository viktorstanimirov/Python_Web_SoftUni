from django.shortcuts import render, redirect

from .forms import CreateCarForm, DeleteCarForm, EditCarForm
from .models import Car
from ..profiles.models import Profile


def create_car(request):
    profile = Profile.objects.all()
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            last_profile = Profile.objects.order_by('-id').values_list('id', flat=True).first()

            if last_profile:
                car.owner_id = last_profile
                car.save()
            return redirect("catalogue")
    else:
        form = CreateCarForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'cars/car-create.html', context)


def catalogue(request):
    profile = Profile.objects.all()
    cars = Car.objects.all()
    total_cars = cars.count()
    context = {
        'cars': cars,
        'total_cars': total_cars,
        'profile': profile,
    }
    return render(request, 'cars/catalogue.html', context)


def car_details(request, pk):
    profile = Profile.objects.all()
    car = Car.objects.get(pk=pk)
    return render(request, 'cars/car-details.html', {'car': car, 'profile': profile})


def edit_car(request, pk):
    profile = Profile.objects.all()
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect("car_details", pk)
    else:
        form = EditCarForm(instance=car)

    context = {
        'car': car,
        'profile': profile,
        "form": form,
    }
    return render(request, 'cars/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect("catalogue")
    else:
        form = DeleteCarForm(instance=car)
    return render(request, 'cars/car-delete.html', {'form': form, 'car': car})
