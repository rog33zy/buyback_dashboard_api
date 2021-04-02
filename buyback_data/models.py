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
        COWPEAS = "cowpeas", _("Cowpeas")

    class VarietyOptions(models.TextChoices):
        KAFUE = "kafue", _("Kafue")
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
        MSANDILE = "msandile", _("Msandile")
        MADAGASCAR = "madagascar", _("Madagascar")
        KABULANGETI = "kabulangeti", _("Kabulangeti")
        LUANGENI = "luangeni", _("Luangeni")
        BOUNTY = "bounty", _("Bounty")
        KALUNGU = "kalungu", _("Kalungu")
        MBERESHI = "mbereshi", _("Mbereshi")
        LUNGWE_BUNGU = "lungwe_bungu", _("Lungwe-Bungu")

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
    total_purchased_amount = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    def __str__(self) -> str:
        return f"{self.camp}-{self.season}-{self.crop}-{self.variety}"
