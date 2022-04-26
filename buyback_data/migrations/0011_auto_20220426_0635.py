# Generated by Django 3.1.7 on 2022-04-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyback_data', '0010_auto_20210521_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buybackdata',
            name='season',
            field=models.CharField(choices=[('2019_2020', '2019-2020'), ('2020_2021', '2020-2021'), ('2021_2022', '2021-2022')], default='2021_2022', max_length=30),
        ),
    ]
