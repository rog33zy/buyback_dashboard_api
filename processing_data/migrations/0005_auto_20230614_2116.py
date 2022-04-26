# Generated by Django 3.1.7 on 2023-06-14 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing_data', '0004_auto_20220426_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processingdata',
            name='season',
            field=models.CharField(choices=[('2019_2020', '2019-2020'), ('2020_2021', '2020-2021'), ('2021_2022', '2021-2022'), ('2022_2023', '2022-2023')], default='2022_2023', max_length=30),
        ),
    ]
