# Generated by Django 5.0.2 on 2024-02-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0004_workspaceimage_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spacecategory',
            options={'verbose_name_plural': 'Space categories'},
        ),
        migrations.RemoveField(
            model_name='workspace',
            name='price',
        ),
        migrations.AddField(
            model_name='spacecategory',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5000, max_digits=10),
            preserve_default=False,
        ),
    ]
