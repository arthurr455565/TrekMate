from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    # Redirect root to the dashboard page which now contains the full layout
    return redirect("core:dashboard")


def dashboard(request):
    return render(request, "core/dashboard.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")

@login_required
def trekker_dashboard(request):
    return render(request, "core/trekker_dashboard.html")

@login_required
def guide_dashboard(request):
    return render(request, "core/guide_dashboard.html")

