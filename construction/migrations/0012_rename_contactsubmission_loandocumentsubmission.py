# Generated by Django 3.2.23 on 2024-01-15 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0011_contactsubmission'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactSubmission',
            new_name='LoanDocumentSubmission',
        ),
    ]