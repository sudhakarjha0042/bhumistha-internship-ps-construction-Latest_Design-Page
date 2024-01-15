from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage, Amenity, Specification, LocationAdvantage
from .forms import ContactForm

def get_filtered_projects():
    projects = Project.objects.all()

    completed_residential = projects.filter(status='Completed', category='Residential')
    ongoing_residential = projects.filter(status='ongoing', category='Residential')
    upcoming_residential = projects.filter(status='upcoming', category='Residential')

    completed_industrial = projects.filter(status='completed', category='Industrial')
    ongoing_industrial = projects.filter(status='ongoing', category='Industrial')
    upcoming_industrial = projects.filter(status='upcoming', category='Industrial')

    completed_commercial = projects.filter(status='completed', category='Commercial')
    ongoing_commercial = projects.filter(status='ongoing', category='Commercial')
    upcoming_commercial = projects.filter(status='upcoming', category='Commercial')
    projects = Project.objects.all()
    project_images = ProjectImage.objects.all()

    return {
        'completed_residential': completed_residential,
        'ongoing_residential': ongoing_residential,
        'upcoming_residential': upcoming_residential,

        'completed_industrial': completed_industrial,
        'ongoing_industrial': ongoing_industrial,
        'upcoming_industrial': upcoming_industrial,

        'completed_commercial': completed_commercial,
        'ongoing_commercial': ongoing_commercial,
        'upcoming_commercial': upcoming_commercial,
        'projects': projects,
        'project_images': project_images,

    }

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
            form.save()
            return render(request, 'construction/success.html')

    else:
        form = ContactForm()

    return render(request, 'construction/contact.html', {'form': form})


def index(request):
    context = get_filtered_projects()
    return render(request, 'construction/index.html', context)

def login_register(request):
    return render(request, 'construction/login-register.html')

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_images = project.projectimage_set.all()
    project_pdfs = project.projectpdf_set.all()
    specifications = Specification.objects.all()
    amenities = Amenity.objects.all()
    location_advantages = LocationAdvantage.objects.filter(project=project)
    category = project.get_category_display()

    context = get_filtered_projects()
    context.update({
        'project': project,
        'project_images': project_images,
        'project_pdfs': project_pdfs,
        'brochure_url': project.brochure.url,
        'specifications': specifications,
        'amenities': amenities,
        'location_advantages': location_advantages,
        'category': category,
    })

    return render(request, 'construction/single-project.html', context)

def projects_view(request):
    context = get_filtered_projects()
    return render(request, 'construction/nav_footer.html', context)

def projects_three(request):
    return render(request, 'construction/projects-three.html')

def projects_two(request):
    return render(request, 'construction/projects-two.html')

def service(request):
    return render(request, 'construction/service.html')

def single_project(request):
    context = get_filtered_projects()
    return render(request, 'construction/single-project.html', context)

def single_service(request):
    return render(request, 'construction/single-service.html')

def gallery(request):
    context = get_filtered_projects()
    projects = Project.objects.all()
    project_images = ProjectImage.objects.all()
            # Query all projects
    projects = Project.objects.all()
    return render(request, 'construction/gallery.html',context)

def calc(request):
    context = get_filtered_projects()
    return render(request, 'construction/calc.html', context)
