# Generated by Django 3.2.9 on 2022-03-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geographicdiv',
            name='geographic_taxon',
        ),
        migrations.AddField(
            model_name='taxonomicunit',
            name='geographic_div',
            field=models.ManyToManyField(to='front.GeographicDiv'),
        ),
    ]
