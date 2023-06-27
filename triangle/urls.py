from django.urls import path

from .views import triangle_hypotenuse

urlpatterns = [
    path('', triangle_hypotenuse, name='triangle_hypotenuse')
]
