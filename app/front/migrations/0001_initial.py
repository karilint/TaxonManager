# Generated by Django 3.2.9 on 2022-02-21 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentator', models.CharField(max_length=100)),
                ('comment_detail', models.TextField(max_length=2000)),
                ('comment_time_stamp', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expert', models.CharField(max_length=100)),
                ('exp_comment', models.CharField(max_length=500)),
                ('update_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ExpertsGeographicDiv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expert_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.expert')),
            ],
        ),
        migrations.CreateModel(
            name='Kingdom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kingdom_name', models.CharField(max_length=20)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('pub_id_prefix', models.CharField(max_length=3, unique=True)),
                ('publication_id', models.IntegerField(primary_key=True, serialize=False)),
                ('reference_author', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=255)),
                ('publication_name', models.CharField(blank=True, max_length=255, null=True)),
                ('listed_pub_date', models.DateTimeField(blank=True, null=True)),
                ('actual_pub_date', models.DateTimeField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, max_length=80, null=True)),
                ('pub_place', models.CharField(blank=True, max_length=40, null=True)),
                ('isbn', models.CharField(blank=True, max_length=16, null=True)),
                ('issn', models.CharField(blank=True, max_length=40, null=True)),
                ('pages', models.CharField(blank=True, max_length=15, null=True)),
                ('pub_comment', models.CharField(blank=True, max_length=500, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('pub_id_prefix', 'publication_id')},
            },
        ),
        migrations.CreateModel(
            name='TaxonAuthorLkp',
            fields=[
                ('taxon_author_id', models.IntegerField(primary_key=True, serialize=False)),
                ('taxon_author', models.CharField(blank=True, max_length=100, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('short_author', models.CharField(blank=True, max_length=100, null=True)),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.kingdom')),
            ],
            options={
                'unique_together': {('taxon_author_id', 'kingdom_id')},
            },
        ),
        migrations.CreateModel(
            name='TaxonomicUnit',
            fields=[
                ('tsn', models.AutoField(primary_key=True, serialize=False)),
                ('unit_ind1', models.CharField(blank=True, max_length=1, null=True)),
                ('unit_name1', models.CharField(max_length=35)),
                ('unit_ind2', models.CharField(blank=True, max_length=1, null=True)),
                ('unit_name2', models.CharField(blank=True, max_length=35, null=True)),
                ('unit_ind3', models.CharField(blank=True, max_length=7, null=True)),
                ('unit_name3', models.CharField(blank=True, max_length=35, null=True)),
                ('unit_ind4', models.CharField(blank=True, max_length=7, null=True)),
                ('unit_name4', models.CharField(blank=True, max_length=35, null=True)),
                ('unnamed_taxon_ind', models.CharField(blank=True, max_length=1, null=True)),
                ('name_usage', models.CharField(blank=True, max_length=12, null=True)),
                ('unaccept_reason', models.CharField(blank=True, max_length=50, null=True)),
                ('credibility_rtng', models.CharField(blank=True, max_length=40, null=True)),
                ('completeness_rtng', models.CharField(blank=True, max_length=10, null=True)),
                ('currency_rating', models.CharField(blank=True, max_length=7, null=True)),
                ('phylo_sort_seq', models.IntegerField(blank=True, null=True)),
                ('initial_time_stamp', models.DateTimeField(blank=True, null=True)),
                ('parent_tsn', models.IntegerField()),
                ('rank_id', models.IntegerField(blank=True, null=True)),
                ('hybrid_author_id', models.IntegerField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('uncertain_prnt_ind', models.CharField(blank=True, max_length=3, null=True)),
                ('n_usage', models.CharField(blank=True, max_length=12, null=True)),
                ('complete_name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TuCommentLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.comment')),
                ('tsn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.taxonomicunit')),
            ],
        ),
        migrations.AddField(
            model_name='taxonomicunit',
            name='comments',
            field=models.ManyToManyField(through='front.TuCommentLink', to='front.Comment'),
        ),
        migrations.AddField(
            model_name='taxonomicunit',
            name='kingdom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.kingdom'),
        ),
        migrations.AddField(
            model_name='taxonomicunit',
            name='taxon_author_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.taxonauthorlkp'),
        ),
        migrations.CreateModel(
            name='SynonymLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tsn', models.IntegerField()),
                ('update_date', models.DateTimeField()),
                ('tsn_accepted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.taxonomicunit')),
            ],
        ),
        migrations.CreateModel(
            name='Hierarchy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hierarchy_string', models.CharField(blank=True, max_length=128, null=True)),
                ('parent_tsn', models.IntegerField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('childrencount', models.IntegerField(blank=True, null=True)),
                ('tsn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.taxonomicunit')),
            ],
        ),
        migrations.CreateModel(
            name='GeographicDiv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geographic_value', models.CharField(blank=True, max_length=45, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('experts', models.ManyToManyField(through='front.ExpertsGeographicDiv', to='front.Expert')),
                ('tsn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.taxonomicunit', unique=True)),
            ],
            options={
                'unique_together': {('tsn', 'geographic_value')},
            },
        ),
        migrations.AddField(
            model_name='expertsgeographicdiv',
            name='geographic_tsn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.geographicdiv', to_field='tsn'),
        ),
        migrations.CreateModel(
            name='TaxonUnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_id', models.IntegerField(blank=True, null=True)),
                ('rank_name', models.CharField(max_length=15)),
                ('dir_parent_rank_id', models.IntegerField(blank=True, null=True)),
                ('req_parent_rank_id', models.IntegerField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('kingdom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.kingdom')),
            ],
            options={
                'unique_together': {('kingdom', 'rank_id')},
            },
        ),
        migrations.CreateModel(
            name='ReferenceLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id_prefix', models.CharField(choices=[('EXP', 'Expert'), ('PUB', 'Publication'), ('SRC', 'Other source')], max_length=3)),
                ('original_desc_ind', models.CharField(max_length=1)),
                ('init_itis_desc_ind', models.CharField(max_length=1)),
                ('change_track_id', models.IntegerField()),
                ('vernacular_name', models.CharField(max_length=80)),
                ('update_date', models.DateTimeField()),
                ('documentation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.publication')),
                ('tsn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.taxonomicunit')),
            ],
            options={
                'unique_together': {('tsn', 'doc_id_prefix', 'documentation_id')},
            },
        ),
    ]
