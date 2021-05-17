# Generated by Django 3.2.2 on 2021-05-16 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='leilao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=10)),
                ('valor_min', models.IntegerField()),
                ('catego', models.CharField(max_length=64)),
            ],
        ),
    ]