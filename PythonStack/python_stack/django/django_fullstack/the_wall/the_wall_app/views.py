from django.shortcuts import render, redirect
from .models import User, Message, Comment
from django.contrib import messages
from django.utils.timezone import now
from datetime import timedelta
import bcrypt

# Create your views here.
def root(request):
    if 'user_id' in request.session:
        return redirect("wall")

    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
       registration_errors = User.objects.registor_validator(request.POST)
       if len(registration_errors) > 0:
          for key,value in registration_errors.items():
             messages.error(request, value, extra_tags="registration")
          return redirect('root')
       else:
          if 'user_id' in request.session:
            return redirect("wall")
          #Create User
          hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), salt=bcrypt.gensalt()).decode()
          this_user = User.objects.create(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            email = request.POST.get('email'),
            password= hashed_pw
           )
          #Create Session 'user_id'
          request.session['user_id'] = this_user.id
          return redirect('wall')
        
    elif request.method == 'GET':
      if 'user_id' not in request.session:
        return redirect("root")
      
      return redirect('wall')

def login(request):
    if request.method == 'POST':
       login_errors = User.objects.login_validator(request.POST)
       if len(login_errors) > 0:
          for key,value in login_errors.items():
             messages.error(request, value, extra_tags="login")
          return redirect('root')
       else:
          if 'user_id' in request.session:
            return redirect("wall")
         
          this_user = User.objects.get(email=request.POST['email'])
          #Create Session 'user_id'
          request.session['user_id'] = this_user.id
          return redirect('wall')
        
    elif request.method == 'GET':
      if 'user_id' not in request.session:
        return redirect("root")
      
      return redirect('wall')

def logout(request):
    request.session.clear()
    return redirect('root')

def wall(request):
    if "user_id" not in request.session:
      return redirect('root')
    
    this_user = User.objects.get(id=request.session.get('user_id'))
    context = {
       'user': this_user,
       'all_messages': Message.objects.all().order_by('-created_at')
    }
    return render(request, 'wall.html', context)

def create_message(request):
    if "user_id" not in request.session:
      return redirect('root')
    
    if request.method == 'POST':
       message_errors = Message.objects.message_validator(request.POST)
       if len(message_errors) > 0:
         for key,value in message_errors.items():
             messages.error(request, value, extra_tags="message_errors")
         return redirect('wall')
       else:
         this_user = User.objects.get(id=request.session.get('user_id'))
         Message.objects.create(
            message=request.POST.get('message'),
            user=this_user
         )
         return redirect('wall')
    return redirect('wall')

def create_comment(request):
   if "user_id" not in request.session:
      return redirect('root')

   if request.method == 'POST':
       comment_errors = Comment.objects.comment_validator(request.POST)
       if len(comment_errors) > 0:
         for key,value in comment_errors.items():
             messages.error(request, value, extra_tags="comment_errors")
         return redirect('wall')
       else:
          this_user = User.objects.get(id=request.session.get('user_id'))
          this_message= Message.objects.get(id=request.POST.get('message_id'))

          Comment.objects.create(
            comment=request.POST.get('comment'),
            created_by_user=this_user,
            message=this_message
          )
          return redirect('wall')
   return redirect('wall')

def delete_message(request, message_id):
   if "user_id" not in request.session:
      return redirect('root')
   
   this_message = Message.objects.get(id=message_id)
   if now() - this_message.created_at <= timedelta(minutes=30):
      this_message.delete()
   else:
       error = "You can only delete messages within 30 minutes of creation."
       messages.error(request, error, extra_tags='delete_message_error')
   return redirect('wall')