# Generated by Django 5.0.2 on 2024-02-19 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspaceimage',
            name='workspace_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspace_images', to='space.workspace'),
        ),
    ]
