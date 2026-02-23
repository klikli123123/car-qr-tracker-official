from model_bakery.recipe import Recipe, seq
from .models import Adres, ProductVariant, Bestelling, Levering

adresRecept = Recipe(
    Adres,
    straat=seq("Straat "),
    nummer=seq("Nr "),
    postcode=seq("2000"),
    stad=seq("Antwerpen"),
    land="België",
)

productvariantRecept = Recipe(
    ProductVariant,
    naam=seq("ProductVariant "),
    kleur="blauw",
    btw_percentage=21,
)

bestellingRecept = Recipe(Bestelling)
leveringRecept = Recipe(Levering)
