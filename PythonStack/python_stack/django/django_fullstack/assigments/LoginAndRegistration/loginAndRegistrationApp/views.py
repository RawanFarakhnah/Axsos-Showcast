from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def root(request):
    if 'user_id' in request.session:
        return redirect('success')
    
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        registration_errors = User.objects.register_validator(request.POST)
        if len(registration_errors):
            for key, value in registration_errors.items():
                messages.error(request, value, extra_tags='registration')
            return redirect("root")
        else:
           #User Session not expired yet
           if 'user_id' in request.session:
               return redirect('success')
          
           hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
           this_user = User.objects.create(
              first_name = request.POST['first_name'],
              last_name = request.POST['last_name'],
              email = request.POST['email'],
              birthdate = request.POST['birthdate'],
              password = hash_pw
           )
         
           #memorize this user using session
           request.session['user_id'] = this_user.id
           return redirect('success')    
    
        return redirect('root')

def login(request):
    if request.method == "POST":
        login_errors = User.objects.login_validator(request.POST)
        if len(login_errors):
            for key, value in login_errors.items():
                messages.error(request, value, extra_tags='login')
            return redirect("root")
        else:
           #User Session not expired yet
           if 'user_id' in request.session:
               return redirect('success')
           
           this_user = User.objects.get(email=request.POST.get('email'))
           request.session['user_id'] = this_user.id
           return redirect('success')
    return redirect('root')

def success(request):
    if 'user_id' not in request.session:
        return redirect('root')
    
    context = {
        'user': User.objects.get(id=request.session.get('user_id'))
    }
    return render(request, "success.html", context)


def logout(request):
    request.session.clear()
    return redirect('root')
