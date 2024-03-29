# Generated by Django 3.2.23 on 2024-01-08 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('rera_no', models.CharField(max_length=20)),
                ('brochure', models.FileField(upload_to='project_brochures/')),
                ('amenities', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='project_pdfs/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='construction.project')),
            ],
        ),
    ]
