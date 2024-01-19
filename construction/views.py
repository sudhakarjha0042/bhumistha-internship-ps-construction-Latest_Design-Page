from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, ProjectImage, Amenity, Specification, LocationAdvantage, BlogPost
from .forms import ContactForm
from .forms import CommentForm,CommentForm

from django.http import HttpResponse
from .models import LoanDocumentSubmission


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

def blog_details(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return render(request, 'construction/blog-details.html', {'post': post, 'form': form})
    else:
        form = CommentForm()

    return render(request, 'construction/blog-details.html', {'post': post, 'form': form})


def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'construction/blog.html', {'blog_posts': blog_posts})

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

def finance(request):
    return render (request, 'construction/finance.html')    

# construction/views.py
def contact_form_submission(request):
    if request.method == 'POST':
        # Process form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        address = request.POST.get('address')
        aadhar_pdf = request.FILES.get('aadhar_pdf')
        pan_pdf = request.FILES.get('pan_pdf')
        salary_slip_pdf = request.FILES.get('salary_slip_pdf')
        form16_pdf = request.FILES.get('form16_pdf')

        # Save data to the database
        submission = LoanDocumentSubmission(
            name=name,
            email=email,
            contact_no=contact_no,
            address=address,
            aadhar_pdf=aadhar_pdf,
            pan_pdf=pan_pdf,
            salary_slip_pdf=salary_slip_pdf,
            form16_pdf=form16_pdf
        )
        submission.save()

        return render(request, 'construction/success.html')  # Redirect to a success page or customize as needed
    return render(request, 'construction/doc_upload.html')


def services(request):
    # Your logic for the services view goes here
    return render(request, 'construction/services.html')

