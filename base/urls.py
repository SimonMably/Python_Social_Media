from django.urls import path

from . import views

urlpatterns = [
    path("", views.initial_home, name="initial-home"),
    path("about", views.about_page, name="about-page"),
    path("features", views.features_page, name="features-page"),
    path("faqs", views.faqs_page, name="faqs-page"),
]
