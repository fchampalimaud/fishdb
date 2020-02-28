from django.urls import path
from .views import get_fish_template

urlpatterns = [
    path("get_fish_template/", get_fish_template, name="get_fish_template"),
]
