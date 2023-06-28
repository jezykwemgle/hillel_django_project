from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_main_paige, name='main_paige'),
    path('triangle/', views.triangle_hypotenuse, name='triangle_hypotenuse'),
    path('person/', views.create_person, name='create_person'),
    path('person/<int:pk> ', views.update_person, name='update_person'),
    path('person-detail/<int:pk>', views.person_detail, name="person_detail"),
    path('person-list/', views.all_person, name='all_person')
]
