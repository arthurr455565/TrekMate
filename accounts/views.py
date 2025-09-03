from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterForm, LoginForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("accounts:login")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Role-based redirection
            if user.role == "trekker":
                return redirect("core:trekker_dashboard")  # Trekker dashboard URL
            elif user.role == "guide":
                return redirect("core:guide_dashboard")    # Guide dashboard URL
            elif user.is_superuser:
                return redirect("/admin/")                 # Admin panel
            else:
                return redirect("core:home")              # Fallback

    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("core:home")
