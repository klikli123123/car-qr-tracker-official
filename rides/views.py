from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Ride


def get_active_ride():
    return Ride.objects.filter(ended_at__isnull=True).order_by("-started_at").first()


def scan(request):
    """
    QR komt hier uit:
    - is er een actieve rit? => toon STOP
    - anders => toon 3 knoppen (Thibeau/Henri/Max)
    """
    active = get_active_ride()
    return render(request, "rides/scan.html", {"active": active})


@require_POST
def start_ride(request, driver: str):
    driver = driver.upper()

    if driver not in ("THIBEAU", "HENRI", "MAX"):
        return redirect("rides:scan")

    if get_active_ride() is not None:
        # Er rijdt al iemand, dus geen nieuwe starten
        return redirect("rides:scan")

    Ride.objects.create(driver=driver, started_at=timezone.now())
    return redirect("rides:scan")


@require_POST
def stop_ride(request):
    active = get_active_ride()
    if active is None:
        return redirect("rides:scan")

    active.ended_at = timezone.now()
    active.save(update_fields=["ended_at"])
    return redirect("rides:scan")


from django.shortcuts import render

# Create your views here.
