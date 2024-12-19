from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Users
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect

@csrf_exempt
def update_user(request, user_id):
    user = get_object_or_404(Users, user_id=user_id)

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.name = request.POST.get('name')
        user.qualification = request.POST.get('qualification')
        user.email = request.POST.get('email')
        user.contact = request.POST.get('contact')
        user.address = request.POST.get('address')
        user.user_type = request.POST.get('user_type')
        user.is_active = request.POST.get('is_active') == 'true'
        user.save()
        return redirect('view_users')

    return render(request, 'update_user.html', {'user': user})

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
            Users.objects.create(
                username=username,
                name=name,
                qualification=qualification,
                email=email,
                contact=contact,
                address=address,
                user_type=user_type,
                is_active=True
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
    users = Users.objects.all()
    return render(request, 'view_users.html', {'users': users})

def delete_user(request, user_id):
    user = get_object_or_404(Users, user_id=user_id)
    if user.is_active:
        user.is_active = False
        user.save()
    return redirect('view_users')
