# Generated by Django 5.0.2 on 2024-02-20 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0003_spacecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspaceimage',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='space.spacecategory'),
            preserve_default=False,
        ),
    ]