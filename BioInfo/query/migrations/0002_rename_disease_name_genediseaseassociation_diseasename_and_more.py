# Generated by Django 4.2.5 on 2023-09-20 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genediseaseassociation',
            old_name='disease_name',
            new_name='diseaseName',
        ),
        migrations.RenameField(
            model_name='genediseaseassociation',
            old_name='gene_symbol',
            new_name='geneSymbol_text',
        ),
    ]
