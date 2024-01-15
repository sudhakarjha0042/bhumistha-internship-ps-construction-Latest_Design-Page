# Generated by Django 3.2.23 on 2024-01-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0010_alter_locationadvantage_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('aadhar_pdf', models.FileField(upload_to='contact_aadhar_pdfs/')),
                ('pan_pdf', models.FileField(upload_to='contact_pan_pdfs/')),
                ('salary_slip_pdf', models.FileField(upload_to='contact_salary_slip_pdfs/')),
                ('form16_pdf', models.FileField(upload_to='contact_form16_pdfs/')),
            ],
        ),
    ]
