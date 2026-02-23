from django.db import models

class Adres(models.Model):
    straat = models.CharField(max_length=200)
    nummer = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    stad = models.CharField(max_length=200)
    land = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.straat} {self.nummer}, {self.postcode} {self.stad}"


class ProductVariant(models.Model):
    naam = models.CharField(max_length=200)
    kleur = models.CharField(max_length=50, blank=True, null=True)
    btw_percentage = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.naam


class Bestelling(models.Model):
    besteld_op = models.DateTimeField(auto_now_add=True)

    # Belangrijk voor de workshop: FK's mogen leeg zijn zodat Bakery ze niet auto-invult
    leveradres = models.ForeignKey(Adres, on_delete=models.CASCADE, blank=True, null=True)
    productvariant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, blank=True, null=True)
    klant = models.ForeignKey("Klant", on_delete=models.CASCADE, blank=True, null=True)
    werknemer = models.ForeignKey("Werknemer", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Bestelling {self.id}"


class Levering(models.Model):
    geleverd_op = models.DateTimeField(blank=True, null=True)

    bestelling = models.ForeignKey(Bestelling, on_delete=models.CASCADE, blank=True, null=True)
    afleveradres = models.ForeignKey(Adres, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Levering {self.id}"


# Create your models here.
class Werknemer(models.Model):
    voornaam = models.CharField(max_length=200)
    achternaam = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.voornaam} {self.achternaam}"


class Klant(models.Model):
    voornaam = models.CharField(max_length=200)
    achternaam = models.CharField(max_length=200)

    adres = models.ForeignKey("Adres", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.voornaam} {self.achternaam}"


class Product(models.Model):
    naam = models.CharField(max_length=200)

    def __str__(self):
        return self.naam
