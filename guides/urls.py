from django.urls import path
from . import views

app_name = "guides"

urlpatterns = [
    path("", views.guide_list, name="list"),
    path("<int:pk>/", views.guide_detail, name="detail"),
    path("profile/create/", views.profile_create, name="create"),
    path("profile/<int:pk>/edit/", views.profile_edit, name="edit"),
]
