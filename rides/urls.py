from django.urls import path
from . import views

app_name = "rides"

from django.urls import path
from . import views

urlpatterns = [
    path("healthz/", views.healthz, name="healthz"),
    path("", views.scan, name="scan"),   # 👈 dit moet hier staan
    path("start/<str:driver>/", views.start_ride, name="start"),
    path("stop/", views.stop_ride, name="stop"),
]