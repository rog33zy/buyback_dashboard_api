from django.db.models.signals import post_save

from django.dispatch import receiver

from .models import ProcessingData

from buyback_data.models import BuybackData


@receiver(post_save, sender=BuybackData)
def update_purchased_amount(sender, instance, **kwargs):
    ProcessingData.objects.update_or_create(
        category=instance.category,
        crop=instance.crop,
        variety=instance.variety,
        season=instance.season,
        camp=instance.camp,
        field_supervisor=instance.field_supervisor,
        defaults={"purchased_weight_mt": instance.actual_yields_weight_mt},
    )
