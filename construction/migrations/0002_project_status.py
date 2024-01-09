# Generated by Django 3.2.23 on 2024-01-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('ongoing', 'Ongoing'), ('future', 'Future Coming')], default='future', max_length=20),
        ),
    ]