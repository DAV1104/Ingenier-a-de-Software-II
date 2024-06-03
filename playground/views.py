from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        hashed_password = make_password(password)

        user = authenticate(username=email, password=hashed_password)

        if user is not None:
            auth_login(request, user)
            return redirect('homepage')  
        else:
            messages.error(request, 'Email o contraseña incorrectos. Por favor, inténtalo de nuevo.')
            return redirect('login') 

    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre')
        nombre_usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        confirmar_contrasena = request.POST.get('confirmar_contrasena')

        if contrasena != confirmar_contrasena:
            error_message = "Las contraseñas no coinciden."
            return render(request, 'registration.html', {'error_message': error_message})

        hashed_password = make_password(contrasena)

        try:
            user = User.objects.create_user(username=email, email=email, password=hashed_password)

            usuario = Usuario.objects.create(nombre_completo=nombre_completo, nombre_usuario=nombre_usuario, email=email, password=hashed_password, user=user)
            print("Usuario creado exitosamente")
            return redirect('succesful_register')
        except Exception as e:
            print("Error al crear usuario:", str(e))
            error_message = "Error al crear usuario. Por favor, inténtalo de nuevo."
            return render(request, 'registration.html', {'error_message': error_message})
    else:
        return render(request, 'register.html')

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