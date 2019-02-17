from django import forms
from .models import Product

class Productform (forms.ModelForm):
    description = forms.CharField(widget = forms.Textarea(
        attrs = {"cols" : "60", "rows": "4"}))
    brands = [
        ("", "Select a brand"),
        ("Carousel Boutique", "Carousel Boutique"),
        ("Sweet Apple Acres", "Sweet Apple Acres"),
        ("Sugarcube Corner", "Sugarcube Corner"),
        ("Canterlot Boutique", "Canterlot Boutique"),
        ("Rarity For You", "Rarity For You"),
        ("Manehattan Mall", "Manehattan Mall"),
        ("Fillydelphia Fliers", "Fillydelphia Fliers"),
        ("Crystal Kingdom Market", "Crystal Kingdom Market"),
        ("Other", "Other")
    ]
    brand = forms.ChoiceField(choices = brands, label = "Manufacturer/Brand")

    class Meta:
        model = Product
        fields = ("brand", "name", "price", "description")