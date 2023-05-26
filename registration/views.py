from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib import messages
from django.db import connection
from django.http import JsonResponse

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Execute SQL query to fetch the user with matching email and password
        query = "SELECT * FROM studentdetails.registration_user WHERE email = %s AND password = %s"
        
        with connection.cursor() as cursor:
            cursor.execute(query,(email, password))
            row = cursor.fetchone()
        if row is not None and row[-1] == 1:
            id, profile_pic, name, email, password, gender,course_prefrence,is_active = row
            request.session['user_id'] = row
            student = {
            'id': row[0],
            'pic': row[1],
            'name': row[2],
            'email': row[3],
            'gender': row[5],
            'course': row[6],
         }
            return render(request, "registration/dashboard.html",{'student':student})
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'registration/login.html')

def home(request):
    return render(request, 'registration/home.html')
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Create a new User instance with the form data
            user = User(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                profile_pic=form.cleaned_data['profile_pic'],
                password=form.cleaned_data['password'],
                gender=form.cleaned_data['gender'],
                course_preferences=form.cleaned_data['course_preferences']
            )
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


def edit_student(request, student_id):
    if request.method == 'POST':
        # Get the updated data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')

        # Update the student record in the database
        cursor = connection.cursor()
        cursor.execute("UPDATE studentdetails.registration_user SET name = %s, email = %s, gender = %s WHERE id = %s", [name, email,gender, student_id])
        connection.commit()

        return render(request, 'registration/login.html')
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM studentdetails.registration_user WHERE id = %s", [student_id])
    row = cursor.fetchone()  # Assuming the query returns only one row

    student = {
        'id': row[0],
        'pic': row[1],
        'name': row[2],
        'email': row[3],
        'gender': row[5],
        'course': row[6],
    }

    return render(request, 'registration/edit_student.html', {'student': student})


def delete_student(request, student_id):
    # Delete the student record from the database
    cursor = connection.cursor()
    cursor.execute("DELETE FROM studentdetails.registration_user WHERE id = %s", [student_id])
    connection.commit()

    return render(request, 'registration/login.html')

def dashboard(request):
    return render(request, 'registration/dashboard.html')