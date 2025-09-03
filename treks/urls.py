from django.urls import path
from .views import trek_list, trek_detail

app_name = "treks"

urlpatterns = [
    path('', trek_list, name='list'),
    path('<slug:slug>/', trek_detail, name='detail'),  # Use slug instead of ID
]
