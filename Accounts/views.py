from django.shortcuts import render,redirect,reverse
from Accounts.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django import forms
from Blogs.models import BlogPost

def signup(request):
    all_blogs = BlogPost.objects.all()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'Accounts/register.html', {'form': form,'all_blogs':all_blogs})


def logout_page(request, *args, **kwargs):
    from django.utils import timezone
    user = request.user
    profile = user.get_profile()
    profile.last_logout = timezone.now()
    profile.save()
    logout(request, *args, **kwargs)