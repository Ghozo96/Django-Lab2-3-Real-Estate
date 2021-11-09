from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in as {}'.format(username))
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Wrong username or password')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username__iexact=username).exists():
                    messages.error(request, 'Username is already taken')
            else:
                if User.objects.filter(email__exact=email).exists():
                    messages.error(request, 'Email is already taken')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'Registered Successfully!')
                    return redirect('accounts:login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged out')
    return redirect('pages:index')

def dashboard(request):
    user_contacts = Contact.objects.all().order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)