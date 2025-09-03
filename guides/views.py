from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import GuideProfile
from .forms import GuideProfileForm

# Check if user is a trekker
def is_trekker(user):
    return getattr(user, "role", None) == "trekker"

# List all guides (for trekkers)
@login_required
def guide_list(request):
    guides = GuideProfile.objects.select_related("user").all()
    return render(request, "guides/guide_list.html", {"guides": guides})

# Guide detail view
@login_required
def guide_detail(request, pk):
    guide = get_object_or_404(GuideProfile, pk=pk)
    return render(request, "guides/guide_detail.html", {"guide": guide})

# Create guide profile (for guides only)
@login_required
def profile_create(request):
    if request.user.role != "guide":
        return redirect("guide_list")  # only guides can create profile

    if request.method == "POST":
        form = GuideProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("guide_detail", pk=profile.pk)
    else:
        form = GuideProfileForm()
    return render(request, "guides/profile_form.html", {"form": form})

# Edit guide profile
@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(GuideProfile, pk=pk)

    if profile.user != request.user:
        return redirect("guide_detail", pk=profile.pk)  # only owner can edit

    if request.method == "POST":
        form = GuideProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("guide_detail", pk=profile.pk)
    else:
        form = GuideProfileForm(instance=profile)
    return render(request, "guides/profile_form.html", {"form": form, "profile": profile})
