from django.db import models

class Specification(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE, default=1)

    def get_description_list(self):
            # Split the description into sentences based on periods
            return [sentence.strip() for sentence in self.description.split('.') if sentence]

    def __str__(self):
        return self.title
    
class LocationAdvantage(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE, default=1)

    def get_description_list(self):
            # Split the description into sentences based on periods
            return [sentence.strip() for sentence in self.description.split('.') if sentence]

    def __str__(self):
        return self.title    

class Amenity(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='amenity_thumbnails/')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
        ('upcoming', 'Upcoming'),
    ]

    title = models.CharField(max_length=255)
    rera_no = models.CharField(max_length=20)
    brochure = models.FileField(upload_to='project_brochures/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    description = models.TextField()
    category = models.CharField(max_length=20, choices=[
        ('Residential', 'Residential'),
        ('Industrial', 'Industrial'),
        ('Commercial', 'Commercial'),
    ])
    def get_description_list(self):
        # Split the description into sentences based on periods
        return [sentence.strip() for sentence in self.description.split('.') if sentence]

    def __str__(self):
        return f'{self.title} - {self.get_status_display()}- {self.category}'

    

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


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=20, choices=[
        ('Residential', 'Residential'),
        ('Industrial', 'Industrial'),
        ('Commercial', 'Commercial'),
    ])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class LoanDocumentSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_no = models.CharField(max_length=20)
    address = models.TextField()
    aadhar_pdf = models.FileField(upload_to='contact_aadhar_pdfs/')
    pan_pdf = models.FileField(upload_to='contact_pan_pdfs/')
    salary_slip_pdf = models.FileField(upload_to='contact_salary_slip_pdfs/')
    form16_pdf = models.FileField(upload_to='contact_form16_pdfs/')

    def __str__(self):
        return self.name
