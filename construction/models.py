# models.py
from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
        ('upcoming', 'Upcoming'),
    ]

    title = models.CharField(max_length=255)
    rera_no = models.CharField(max_length=20)
    brochure = models.FileField(upload_to='project_brochures/')
    amenities = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')

    def __str__(self):
        return f'{self.title} - {self.get_status_display()}'


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f'Image {self.id}'


class ProjectPDF(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='project_pdfs/')

    def __str__(self):
        return f'PDF for {self.project.title}'
