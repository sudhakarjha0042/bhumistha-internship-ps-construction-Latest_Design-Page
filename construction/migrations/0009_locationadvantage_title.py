# Generated by Django 3.2.23 on 2024-01-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0008_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationadvantage',
            name='title',
            field=models.CharField(default=404, max_length=255),
            preserve_default=False,
        ),
    ]
