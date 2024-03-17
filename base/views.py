from django.shortcuts import redirect, render


# Create your views here.
def initial_home(request):
    return render(request, "base/entryway.html", {})


def about_page(request):
    return render(request, "base/about.html")


def features_page(request):
    return render(request, "base/features.html")


def faqs_page(request):
    return render(request, "base/faqs.html")
