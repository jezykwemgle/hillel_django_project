from math import pow, sqrt

from django.shortcuts import render

from .forms import TriangleForm


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
