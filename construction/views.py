from django.shortcuts import render
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

def projects_one(request):
    return render(request, 'construction/projects-one.html')

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
    return render(request, 'construction/gallery.html')




