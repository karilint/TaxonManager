# Generated by Django 3.2.9 on 2022-02-13 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_auto_20220213_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kingdom',
            name='update_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='taxonunittype',
            name='update_date',
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name='TaxonomicUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_ind1', models.CharField(max_length=100)),
                ('unit_name1', models.CharField(max_length=100)),
                ('unit_ind2', models.CharField(max_length=100)),
                ('unit_name2', models.CharField(max_length=100)),
                ('unit_ind3', models.CharField(max_length=100)),
                ('unit_name3', models.CharField(max_length=100)),
                ('unit_ind4', models.CharField(max_length=100)),
                ('unnamed_taxon_ind', models.CharField(max_length=100)),
                ('name_usage', models.CharField(max_length=100)),
                ('unaccept_reason', models.CharField(max_length=100)),
                ('credibility_rtng', models.CharField(max_length=100)),
                ('completeness_rtng', models.CharField(max_length=100)),
                ('currency_rating', models.CharField(max_length=100)),
                ('phylo_sort_seq', models.IntegerField(default=0)),
                ('initial_time_stamp', models.DateTimeField()),
                ('parent_tsn', models.IntegerField(default=0)),
                ('taxon_author_id', models.IntegerField(default=0)),
                ('rank_id', models.IntegerField(default=0)),
                ('hybrid_author_id', models.IntegerField(default=0)),
                ('update_date', models.DateTimeField()),
                ('uncertain_prnt_ind', models.CharField(max_length=100)),
                ('n_usage', models.CharField(max_length=100)),
                ('complete_name', models.CharField(max_length=100)),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.kingdom')),
            ],
        ),
    ]
