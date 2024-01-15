from django.contrib import admin
from .models import Project, ProjectImage, ProjectPDF, ContactMessage, Amenity, Specification, LocationAdvantage, LoanDocumentSubmission

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage

class ProjectPDFInline(admin.TabularInline):
    model = ProjectPDF

class AmenityInline(admin.TabularInline):
    model = Amenity
    extra = 1  # Number of empty forms to display, adjust as needed

class LocationAdvantageInline(admin.TabularInline):
    model = LocationAdvantage
    extra = 1  # Number of empty forms to display, adjust as needed

class SpecificationInline(admin.TabularInline):
    model = Specification
    extra = 1  # Number of empty forms to display, adjust as needed

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, ProjectPDFInline, AmenityInline, SpecificationInline, LocationAdvantageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactMessage)
admin.site.register(Amenity)
admin.site.register(Specification)
admin.site.register(LocationAdvantage)
admin.site.register(LoanDocumentSubmission)
