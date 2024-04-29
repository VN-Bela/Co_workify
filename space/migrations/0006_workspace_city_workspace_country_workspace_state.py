# Generated by Django 5.0.2 on 2024-04-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0005_alter_spacecategory_options_remove_workspace_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='workspace',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='workspace',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
