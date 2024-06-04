from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib.auth.hashers import make_password
from .forms import UserRegistrationForm, UserLoginForm
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = UserLoginForm()

    return render(request, "login.html", {"form": form})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("hello")
            form.save()
            return redirect('homepage')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration.html', {'form': form})



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def trainers(request):
    return render(request, 'trainers.html')

def courses(request):
    return render(request, 'courses.html')

def contact(request):
    return render(request, 'contact.html')

def course_details(request):
    return render(request, 'course-details.html')

def course_section(request):
    return render(request, 'course-section.html')

def homepage(request):
    return render(request, 'homepage.html')

def starter_page(request):
    return render(request, 'starter_page.html')

def succesful_register(request):
    return render(request, 'successful_register.html')