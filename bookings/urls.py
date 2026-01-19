from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('create/', views.booking_create, name='booking_create'),
    path('trek-booking/', views.trek_booking_create, name='trek_booking_create'),
    path('<int:booking_id>/review/', views.add_review, name='add_review'),
]
