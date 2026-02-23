from django.db import models
from django.utils import timezone


class Ride(models.Model):
    DRIVER_CHOICES = [
        ("THIBEAU", "Thibeau"),
        ("HENRI", "Henri"),
        ("MAX", "Max"),
    ]

    driver = models.CharField(max_length=20, choices=DRIVER_CHOICES)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.driver} | {self.started_at} -> {self.ended_at or 'ACTIVE'}"


class Fine(models.Model):
    happened_at = models.DateTimeField(help_text="Datum + tijd van de boete.")
    driver_at_time = models.CharField(max_length=20, blank=True, editable=False)
    ride = models.ForeignKey(Ride, null=True, blank=True, on_delete=models.SET_NULL)

    notes = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fine {self.happened_at} ({self.driver_at_time or 'unknown'})"

    def resolve_driver(self):
        t = self.happened_at
        if timezone.is_naive(t):
            t = timezone.make_aware(t, timezone.get_current_timezone())

        ride = Ride.objects.filter(
            started_at__lte=t
        ).filter(
            models.Q(ended_at__gte=t) | models.Q(ended_at__isnull=True)
        ).order_by("-started_at").first()

        self.ride = ride
        self.driver_at_time = ride.driver if ride else ""

    def save(self, *args, **kwargs):
        self.resolve_driver()
        super().save(*args, **kwargs)
# Create your models here.
