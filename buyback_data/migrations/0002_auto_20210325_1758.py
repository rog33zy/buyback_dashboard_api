# Generated by Django 3.1.7 on 2021-03-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyback_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buybackdata',
            old_name='total_yield_bought_weight',
            new_name='actual_yields_weight_mt',
        ),
        migrations.RenameField(
            model_name='buybackdata',
            old_name='total_yield_estimate',
            new_name='yields_estimates_weight_mt',
        ),
        migrations.AlterField(
            model_name='buybackdata',
            name='category',
            field=models.CharField(choices=[('seed', 'Seed'), ('commercial', 'Commercial'), ('foundation_farm', 'Foundation Farm')], default='seed', max_length=30),
        ),
        migrations.AlterField(
            model_name='buybackdata',
            name='crop',
            field=models.CharField(choices=[('soybeans', 'Soybeans'), ('groundnuts', 'Groundnuts'), ('cowpeas', 'Cowpeas')], default='soybeans', max_length=30),
        ),
        migrations.AlterField(
            model_name='buybackdata',
            name='season',
            field=models.CharField(choices=[('2019_2020', '2019-2020'), ('2020_2021', '2020-2021')], default='2020_2021', max_length=30),
        ),
        migrations.AlterField(
            model_name='buybackdata',
            name='variety',
            field=models.CharField(choices=[('kafue', 'Kafue'), ('mgv4', 'MGV4'), ('mgv5', 'MGV5'), ('mgv7', 'MGV7'), ('mgv8', 'MGV8'), ('wamusanga', 'Wamusanga'), ('lupande', 'Lupande'), ('aqua', 'Aqua'), ('chishango', 'Chishango'), ('lutembwe', 'Lutembwe'), ('bubebe', 'Bubebe'), ('msandile', 'Msandile'), ('madagascar', 'Madagascar'), ('kabulangeti', 'Kabulangeti'), ('luangeni', 'Luangeni'), ('bounty', 'Bounty'), ('kalungu', 'Kalungu'), ('mbereshi', 'Mbereshi'), ('lungwe_bungu', 'Lungwe-Bungu')], default='kafue', max_length=30),
        ),
    ]