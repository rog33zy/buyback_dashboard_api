from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.
class BuybackData(models.Model):
    class CategoryOptions(models.TextChoices):
        SOURCE = "source", _("Source")
        SEED = "seed", _("Seed")
        COMMERCIAL = "commercial", _("Commercial")
        OTHER = "foundation_farm", _("Foundation Farm")

    class CropOptions(models.TextChoices):
        SOYBEANS = "soybeans", _("Soybeans")
        GROUNDNUTS = "groundnuts", _("Groundnuts")
        BEANS = "beans", _("Beans")
        COWPEAS = "cowpeas", _("Cowpeas")
        PIGEON_PEA = "pigeon_pea", _("Pigeon-Pea")
        GREEN_GRAM = "green_gram", _("Green-Gram")

    class VarietyOptions(models.TextChoices):
        KAFUE = "kafue", _("Kafue")
        TGX = "tgx", _("TGX")
        MGV4 = "mgv4", _("MGV4")
        MGV5 = "mgv5", _("MGV5")
        MGV7 = "mgv7", _("MGV7")
        MGV8 = "mgv8", _("MGV8")
        WAMUSANGA = "wamusanga", _("Wamusanga")
        LUPANDE = "lupande", _("Lupande")
        AQUA = "aqua", _("Aqua")
        CHISHANGO = "chishango", _("Chishango")
        LUTEMBWE = "lutembwe", _("Lutembwe")
        BUBEBE = "bubebe", _("Bubebe")
        BLACK_EYED = "black_eyed", _("Black-Eyed")
        MSANDILE = "msandile", _("Msandile")
        MADAGASCAR = "madagascar", _("Madagascar")
        KABULANGETI = "kabulangeti", _("Kabulangeti")
        LUANGENI = "luangeni", _("Luangeni")
        BOUNTY = "bounty", _("Bounty")
        KALUNGU = "kalungu", _("Kalungu")
        MBERESHI = "mbereshi", _("Mbereshi")
        LUNGWE_BUNGU = "lungwe_bungu", _("Lungwe-Bungu")
        MTHAWA_JUNE = "mthawa_june", _("Mthawa-June")
        SHENI = "sheni", _("Sheni")

    class SeasonOptions(models.TextChoices):
        TWENTY_NINETEEN_TWENTY_TWENTY = "2019_2020", _("2019-2020")
        TWENTY_TWENTY_TWENTY_TWENTY_ONE = "2020_2021", _("2020-2021")

    category = models.CharField(max_length=30, choices=CategoryOptions.choices, default=CategoryOptions.SEED)
    crop = models.CharField(max_length=30, choices=CropOptions.choices, default=CropOptions.SOYBEANS)
    variety = models.CharField(max_length=30, choices=VarietyOptions.choices, default=VarietyOptions.KAFUE)
    season = models.CharField(
        max_length=30, choices=SeasonOptions.choices, default=SeasonOptions.TWENTY_TWENTY_TWENTY_TWENTY_ONE
    )
    camp = models.CharField(max_length=50, blank=True)
    field_supervisor = models.CharField(max_length=100, blank=True)
    yields_estimates_weight_mt = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    actual_yields_weight_mt = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    total_farmers_purchased_from = models.PositiveIntegerField(default=0)
    total_hectares_purchased_from = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    total_purchased_amount_zmw = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    total_purchased_amount_usd = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    last_updated = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.category}-{self.camp}-{self.season}-{self.crop}-{self.variety}"
