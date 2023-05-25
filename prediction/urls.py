from django.urls import path

from . import views

urlpatterns = [
    path("", views.user_form, name="user_form"),
    # path("/result", views.index, name)
]