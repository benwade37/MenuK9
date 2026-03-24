from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

from .forms import UserRegisterForm, ProfileUpdateForm, VaccinationForm
from .models import Profile, Vaccination


# ✅ Define formset at top level
VaccinationFormSet = modelformset_factory(
    Vaccination,
    form=VaccinationForm,
    extra=1,
    can_delete=True
)


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

    # Ensure Profile exists
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        formset = VaccinationFormSet(
            request.POST,
            queryset=Vaccination.objects.filter(profile=request.user.profile)
        )

        if form.is_valid() and formset.is_valid():
            form.save()

            instances = formset.save(commit=False)
            for instance in instances:
                instance.profile = request.user.profile
                instance.save()

            # Handle deletes
            for obj in formset.deleted_objects:
                obj.delete()

            return redirect("user-profile")

    else:
        form = ProfileUpdateForm(instance=request.user.profile)

        formset = VaccinationFormSet(
            queryset=Vaccination.objects.filter(profile=request.user.profile)
        )

    return render(request, "users/profile.html", {
        "form": form,
        "formset": formset
    })