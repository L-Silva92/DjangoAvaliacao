# Generated by Django 3.2.2 on 2021-05-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_categ_leilao'),
    ]

    operations = [
        migrations.AddField(
            model_name='leilao',
            name='dono',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]