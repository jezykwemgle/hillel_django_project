from math import pow, sqrt

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PersonForm, TriangleForm
from .models import Person


def view_main_paige(request):
    return render(request, 'main_paige.html')


def triangle_hypotenuse(request):
    if request.method == 'POST':
        form = TriangleForm(request.POST)
        if form.is_valid():
            c1 = form.get_cathetus1()
            c2 = form.get_cathetus2()
            hypotenuse = sqrt(pow(c1, 2) + pow(c2, 2))
            return render(request, 'hypotenuse.html', {'form': form, 'hypotenuse': hypotenuse})
    else:
        form = TriangleForm()
        return render(request, 'hypotenuse.html', {'form': form})


def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, 'Person has been created')
            return redirect(reverse('person_detail', args=[obj.pk]))
    form = PersonForm()
    return render(request, 'create_person.html', {'form': form})


def person_detail(request, pk):
    obj = get_object_or_404(Person, pk=pk)
    return render(request, 'person_detail.html', {'obj': obj})


def update_person(request, pk):
    obj = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=obj)
        if form.is_valid():
            if form.has_changed():
                obj = form.save()
                messages.success(request, "Person has been updated")
            else:
                messages.info(request, "Person is up to date")
        return redirect(reverse('person_detail', args=[obj.pk]))
    else:
        form = PersonForm()
        return render(request, 'update_person.html', {'form': form})


def all_person(request):
    p_list = Person.objects.all()
    return render(request, 'all_person.html', {'obj': p_list})
