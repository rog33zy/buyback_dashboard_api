# Generated by Django 3.1.7 on 2021-05-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyback_data', '0008_auto_20210504_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='buybackdata',
            name='total_farmers',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
