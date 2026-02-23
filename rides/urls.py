from django.urls import path
from . import views

app_name = "rides"

urlpatterns = [
    path("", views.scan, name="scan"),
    path("start/<str:driver>/", views.start_ride, name="start"),
    path("stop/", views.stop_ride, name="stop"),
]