# staff/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_list, name='all-staff'),
    path('add-staff/', views.add_staff, name='addstaff'),
    path('update-staff/<str:id>/', views.update_staff, name='update-staff'),
    path('delete-staff/<str:id>/', views.delete_staff, name='delete-staff'),
]
