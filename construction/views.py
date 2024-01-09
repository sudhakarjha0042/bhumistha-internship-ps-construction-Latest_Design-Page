from django.shortcuts import render,get_object_or_404
from .models import Project, ProjectImage
from .forms import ContactForm

def about(request):
    return render(request, 'construction/about.html')

def blog_details(request):
    return render(request, 'construction/blog-details.html')

def blog(request):
    return render(request, 'construction/blog.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return render(request, 'construction/success.html')  # Create a success.html template

    else:
        form = ContactForm()

    return render(request, 'construction/contact.html', {'form': form})

def gallery(request):
    return render(request, 'construction/gallery.html')

def index(request):
    return render(request, 'construction/index.html')

def login_register(request):
    return render(request, 'construction/login-register.html')

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_images = project.projectimage_set.all()
    project_pdfs = project.projectpdf_set.all()

    return render(request, 'construction/single-project.html', {
        'project': project,
        'project_images': project_images,
        'project_pdfs': project_pdfs,
        'brochure_url': project.brochure.url,  # Add the brochure URL to the context
    })

def projects_three(request):
    return render(request, 'construction/projects-three.html')

def projects_two(request):
    return render(request, 'construction/projects-two.html')

def service(request):
    return render(request, 'construction/service.html')

def single_project(request):
    return render(request, 'construction/single-project.html')

def single_service(request):
    return render(request, 'construction/single-service.html')

def gallery(request):
    projects = Project.objects.all()
    project_images = ProjectImage.objects.all()
    print(project_images)
    return render(request, 'construction/gallery.html', {'projects': projects, 'project_images': project_images})




