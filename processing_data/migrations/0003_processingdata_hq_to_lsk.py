# Generated by Django 3.1.7 on 2021-05-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing_data', '0002_remove_processingdata_purchased_amount_zmw'),
    ]

    operations = [
        migrations.AddField(
            model_name='processingdata',
            name='hq_to_lsk',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
