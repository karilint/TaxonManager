# Generated by Django 3.2.9 on 2022-03-24 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0006_alter_taxonomicunit_reference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxonomicunit',
            name='reference',
        ),
        migrations.AddField(
            model_name='taxonomicunit',
            name='reference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='front.reference'),
        ),
    ]