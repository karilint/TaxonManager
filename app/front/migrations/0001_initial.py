# Generated by Django 3.2.9 on 2022-02-13 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kingdom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kingdom_name', models.CharField(max_length=100)),
                ('update_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TaxonUnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_id', models.IntegerField(default=0)),
                ('rank_name', models.CharField(max_length=100)),
                ('dir_parent_rank_id', models.IntegerField(default=0)),
                ('req_parent_rank_id', models.IntegerField(default=0)),
                ('update_date', models.DateTimeField()),
                ('kingdom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.kingdom')),
            ],
        ),
    ]
