from django.urls import path
from . import views

app_name = 'construction'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('', views.index, name='index'),
    path('login-register/', views.login_register, name='login_register'),
    path('projects-one/', views.projects_one, name='projects_one'),
    path('projects-three/', views.projects_three, name='projects_three'),
    path('projects-two/', views.projects_two, name='projects_two'),
    path('service/', views.service, name='service'),
    path('single-project/', views.single_project, name='single_project'),
    path('single-service/', views.single_service, name='single_service'),
]
