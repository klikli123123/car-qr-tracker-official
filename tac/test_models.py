from model_bakery import baker

def maak_data():
    for _ in range(20):
        baker.make_recipe("tac.adresRecept")

    for _ in range(10):
        baker.make_recipe("tac.productvariantRecept")

    for _ in range(30):
        baker.make_recipe("tac.bestellingRecept")
        baker.make_recipe("tac.leveringRecept")

import random
from .models import Adres, ProductVariant, Bestelling, Levering

def link_data():
    adressen = list(Adres.objects.all())
    varianten = list(ProductVariant.objects.all())

    for b in Bestelling.objects.all():
        b.leveradres = random.choice(adressen)
        b.productvariant = random.choice(varianten)
        b.save()

    for l in Levering.objects.all():
        l.bestelling = random.choice(list(Bestelling.objects.all()))
        l.afleveradres = random.choice(adressen)
        l.save()
import requests
from .models import Klant

def import_klanten(aantal=20):
    data = requests.get(f"https://randomuser.me/api/?results={aantal}").json()
    for u in data["results"]:
        Klant.objects.create(
            voornaam=u["name"]["first"],
            achternaam=u["name"]["last"],
        )
import requests
from .models import Werknemer

def import_werknemers(aantal=10):
    data = requests.get(f"https://randomuser.me/api/?results={aantal}").json()
    for u in data["results"]:
        Werknemer.objects.create(
            voornaam=u["name"]["first"],
            achternaam=u["name"]["last"],
        )
import requests
from .models import Product

def import_producten(aantal=30):
    data = requests.get("https://dummyjson.com/products?limit=30").json()
    for p in data["products"][:aantal]:
        Product.objects.create(naam=p["title"])
import random
from .models import Adres, Klant, Werknemer, Product, ProductVariant, Bestelling

def link_oef11():
    adressen = list(Adres.objects.all())
    klanten = list(Klant.objects.all())
    werknemers = list(Werknemer.objects.all())
    producten = list(Product.objects.all())
    varianten = list(ProductVariant.objects.all())

    for k in klanten:
        k.adres = random.choice(adressen)
        k.save()

    for v in varianten:
        v.product = random.choice(producten)
        v.save()

    for b in Bestelling.objects.all():
        b.klant = random.choice(klanten)
        b.werknemer = random.choice(werknemers)
        b.save()
