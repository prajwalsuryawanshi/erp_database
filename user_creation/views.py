from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.db import IntegrityError

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        qualification = request.POST.get('qualification')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        user_type = request.POST.get('user_type')

        errors = []

        if not username:
            errors.append("Username is required.")
        if not name:
            errors.append("Name is required.")
        if not qualification:
            errors.append("Qualification is required.")
        if not email:
            errors.append("Email is required.")
        if not contact:
            errors.append("Contact is required.")
        if not address:
            errors.append("Address is required.")
        if not user_type:
            errors.append("User Type is required.")

        if errors:
            return render(request, 'create_user.html', {'errors': errors})

        try:
            User.objects.create(
                username=username,
                name=name,
                qualification=qualification,
                email=email,
                contact=contact,
                address=address,
                user_type=user_type
            )
            return render(request, 'user_created.html', {'username': username})
        except IntegrityError as e:
            if 'username' in str(e):
                errors.append("This username is already taken. Please choose another.")
            else:
                errors.append("An error occurred while creating the user.")
            return render(request, 'create_user.html', {'errors': errors})

    return render(request, 'create_user.html')

def view_users(request):
    users = User.objects.all()
    return render(request, 'view_users.html', {'users': users})