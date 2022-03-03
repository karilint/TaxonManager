# Generated by Django 3.2.9 on 2022-03-03 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geographicdiv',
            old_name='tsn',
            new_name='taxon_id',
        ),
        migrations.RenameField(
            model_name='hierarchy',
            old_name='parent_tsn',
            new_name='parent_id',
        ),
        migrations.RenameField(
            model_name='hierarchy',
            old_name='tsn',
            new_name='taxon_id',
        ),
        migrations.RenameField(
            model_name='referencelink',
            old_name='tsn',
            new_name='taxon_id',
        ),
        migrations.RenameField(
            model_name='synonymlink',
            old_name='tsn',
            new_name='synonym_id',
        ),
        migrations.RenameField(
            model_name='synonymlink',
            old_name='tsn_accepted',
            new_name='taxon_id_accepted',
        ),
        migrations.RenameField(
            model_name='taxonomicunit',
            old_name='parent_tsn',
            new_name='parent_id',
        ),
        migrations.RenameField(
            model_name='taxonomicunit',
            old_name='tsn',
            new_name='taxon_id',
        ),
        migrations.RenameField(
            model_name='tucommentlink',
            old_name='tsn',
            new_name='taxon_id',
        ),
        migrations.RemoveField(
            model_name='expertsgeographicdiv',
            name='geographic_tsn',
        ),
        migrations.AddField(
            model_name='expertsgeographicdiv',
            name='geographic_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='front.geographicdiv', to_field='taxon_id'),
        ),
        migrations.AlterUniqueTogether(
            name='geographicdiv',
            unique_together={('taxon_id', 'geographic_value')},
        ),
        migrations.AlterUniqueTogether(
            name='referencelink',
            unique_together={('taxon_id', 'doc_id_prefix', 'documentation_id')},
        ),
    ]
