# Generated by Django 3.1.7 on 2023-06-19 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyback_data', '0012_auto_20230614_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buybackdata',
            name='variety',
            field=models.CharField(choices=[('kafue', 'Kafue'), ('tgx', 'TGX'), ('mgv4', 'MGV4'), ('mgv5', 'MGV5'), ('mgv7', 'MGV7'), ('mgv8', 'MGV8'), ('wamusanga', 'Wamusanga'), ('lupande', 'Lupande'), ('aqua', 'Aqua'), ('chishango', 'Chishango'), ('lutembwe', 'Lutembwe'), ('bubebe', 'Bubebe'), ('black_eyed', 'Black-Eyed'), ('msandile', 'Msandile'), ('madagascar', 'Madagascar'), ('kabulangeti', 'Kabulangeti'), ('luangeni', 'Luangeni'), ('bounty', 'Bounty'), ('kalungu', 'Kalungu'), ('mbereshi', 'Mbereshi'), ('lungwe_bungu', 'Lungwe-Bungu'), ('mthawa_june', 'Mthawa-June'), ('sheni', 'Sheni'), ('tikolore', 'Tikolore'), ('lui', 'Lui'), ('lua_45', 'Lua-45'), ('lunga', 'Lunga'), ('machili', 'Machili'), ('gna_101', 'GNA-101')], default='kafue', max_length=30),
        ),
    ]
