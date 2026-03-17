from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile


def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("user-login")

    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    # Ensure the Profile exists for the logged-in user
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("user-profile")
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "form": form,
    }
    return render(request, "users/profile.html", context)