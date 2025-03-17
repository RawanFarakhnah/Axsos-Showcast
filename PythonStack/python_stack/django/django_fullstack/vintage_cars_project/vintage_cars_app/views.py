from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Car
import bcrypt

# Create your views here.
def root(request):
    if 'user_id' in request.session:
        return redirect("cars")

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
            return redirect("cars")
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
          return redirect('cars')
        
    elif request.method == 'GET':
      if 'user_id' not in request.session:
        return redirect("root")
      
      return redirect('cars')

def login(request):
    if request.method == 'POST':
       login_errors = User.objects.login_validator(request.POST)
       if len(login_errors) > 0:
          for key,value in login_errors.items():
             messages.error(request, value, extra_tags="login")
          return redirect('root')
       else:
          if 'user_id' in request.session:
            return redirect("cars")
         
          this_user = User.objects.get(email=request.POST['email'])
          #Create Session 'user_id'
          request.session['user_id'] = this_user.id
          return redirect('cars')
        
    elif request.method == 'GET':
      if 'user_id' not in request.session:
        return redirect("root")
      
      return redirect('cars')

def logout(request):
    request.session.clear()
    return redirect('root')

def cars(request):
    if "user_id" not in request.session:
      return redirect('root')
    
    this_user = User.objects.get(id=request.session.get('user_id'))
    context = {
       'user': this_user,
       'all_cars': Car.objects.all()
    }
    return render(request, 'cars.html', context)

def new_car(request):
   if "user_id" not in request.session:
      return redirect('root')
   
   if request.method == "GET":
       return render(request, "create.html")
   
def create_car(request):
   if "user_id" not in request.session:
      return redirect('root')
   
   if request.method == "POST":
      create_car_errors = Car.objects.basic_validator(request.POST)
      if len(create_car_errors) > 0:
          for key,value in create_car_errors.items():
             messages.error(request, value, extra_tags="create_car_errors")
          return redirect('new_car')
      else:
          this_user = User.objects.get(id=request.session.get('user_id'))
          Car.objects.create(
              price = request.POST['price'],
              model = request.POST['model'],
              make = request.POST['make'],
              year = request.POST['year'],
              seller_contact= request.POST['seller_contact'],
              description = request.POST['description'],
              seller = this_user,              
          )
          return redirect('cars')
   return redirect('cars')
 
def edit_car(request, car_id):
    if "user_id" not in request.session:
      return redirect('root')
    
    this_user = User.objects.get(id=request.session.get("user_id"))
    this_car = Car.objects.get(id=car_id)
   
    #validate ablite to edit (owner)
    if this_user != this_car.seller : 
        return redirect("cars")
    else:
        context = {
        "car": this_car
        }
        return render(request, "edit.html", context)
   
def update_car(request, car_id):
   if "user_id" not in request.session:
      return redirect('root')
   
   this_user = User.objects.get(id=request.session.get("user_id"))
   this_car = Car.objects.get(id=car_id)
   
   #validate ablite to update (owner)
   if this_user != this_car.seller : 
        return redirect("cars")
   else:
      if request.method == "POST":
         update_car_errors = Car.objects.basic_validator(request.POST)
         if len(update_car_errors) > 0:
             for key,value in update_car_errors.items():
                messages.error(request, value, extra_tags="update_car_errors")
             return redirect('edit', car_id=car_id)
         else:
             this_user = User.objects.get(id=request.session.get('user_id'))
             this_car = Car.objects.get(id=car_id)
             this_car.price = request.POST['price']
             this_car.model = request.POST['model']
             this_car.make = request.POST['make']
             this_car.year = request.POST['year']
             this_car.seller_contact= request.POST['seller_contact']
             this_car.description = request.POST['description']
             this_car.seller = this_user            
             this_car.save()
             return redirect('cars')
      return redirect('cars')

def view_car(request, car_id):
    if "user_id" not in request.session:
      return redirect('root')
    
    this_user = User.objects.get(id=request.session.get("user_id"))
    this_car = Car.objects.get(id=car_id)
   
    #validate ablite to view and order (not owner) 
    if this_user == this_car.seller : 
        return redirect("cars")
    else:
      context = {
          "car": this_car
      }
      return render(request, "view.html", context)

def destroy_car(request, car_id):
    if "user_id" not in request.session:
      return redirect('root')
    
    this_user = User.objects.get(id=request.session.get("user_id"))
    this_car = Car.objects.get(id=car_id)
   
    #validate ablite to delete (owner)
    if this_user != this_car.seller: 
        return redirect("cars")
    else:
      this_car.delete()
      return redirect('cars')

def order_car(request, car_id):
     if "user_id" not in request.session:
      return redirect('root')
     
     this_user = User.objects.get(id=request.session.get("user_id"))
     this_car = Car.objects.get(id=car_id)
   
     #validate ablite to view and order 
     if this_user == this_car.seller: 
        return redirect("cars")
     else:
        this_car.purchaser = this_user
        this_car.status = True #SOLD
        this_car.save()
        return redirect('cars')

def purchase_orders(request):
   if "user_id" not in request.session:
      return redirect('root')
   
   user_id =request.session.get('user_id')
   this_user = User.objects.get(id=user_id)

   context = {
      'user': this_user,
      'my_purchased_cars': Car.objects.filter(purchaser__id=user_id)
   }
   return render(request, 'purchase_orders.html', context)

def cancle_purchase_order(request, car_id):
     if "user_id" not in request.session:
      return redirect('root')
     
     this_user = User.objects.get(id=request.session.get("user_id"))
     this_car = Car.objects.get(id=car_id)
   
     #validate ablite to view and order (owner)
     if this_user != this_car.seller: 
        return redirect("cars")
     else:
        this_user.purchas_cars.remove(this_car)
        this_user.save()
        
        this_car.status = False #For SAles
        this_car.save()
        return redirect('cars')