# Generated by Django 3.2.9 on 2022-04-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20220330_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxonauthorlkp',
            name='geographic_div',
        ),
        migrations.AddField(
            model_name='expert',
            name='geographic_div',
            field=models.ManyToManyField(to='front.GeographicDiv'),
        ),
    ]
