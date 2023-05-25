from django.urls import path

from . import views

urlpatterns = [
    path("features", views.feature_details, name="feature_details"),
    path("inspect", views.first_n_rows, name="first_n_rows"),
    path("statistics", views.stats, name="statistics")
]