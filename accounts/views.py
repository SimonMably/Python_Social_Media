from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm
from .models import User


def login_page(request):
    # TODO: Does not seem to work, compare with login function in study_buddy project
    page = "login"

    if request.user.is_authenticated:
        return redirect("user-feed")

    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")

        print(email, password)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "User does not exist")

        user = authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            print(user)
            return redirect("user-feed")
        else:
            messages.error(request, "Username or password is wrong. Try again.")

    context = {"page": page}
    return render(request, "accounts/register_login.html", context)


def logout_user(request):
    # TODO: Test
    logout(request)
    return redirect("initial-home")


def register_page(request):
    page = "register"

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("user-feed")
        else:
            messages.error(request, "An error occurred during registration.")

    context = {"page": page, "form": form}
    return render(request, "accounts/register_login.html", context)


def user_feed(request):

    context = {}
    return render(request, "accounts/user_feed.html", context)
