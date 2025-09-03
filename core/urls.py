from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("dashboard/trekker/", views.trekker_dashboard, name="trekker_dashboard"),
    path("dashboard/guide/", views.guide_dashboard, name="guide_dashboard"),
]
