from django.shortcuts import render, redirect, HttpResponse
from .models import Course, MakeDescription
from django.contrib import messages

# Create your views here.
def main(request):
    return redirect('root')

def root(request):
    if request.method == "GET":
       context = {
           'all_courses' : Course.objects.all()
       }
       return render(request, "index.html", context)

def create(request):
    if request.method == 'POST':
       errors = Course.objects.basic_validator(request.POST)
       if len(errors) > 0:
          for key, value in errors.items():
             messages.error(request, value)
          return redirect('root')
       else: 
         makeDescription = None
         if request.POST['description']:
            makeDescription = MakeDescription.objects.create(description= request.POST['description'])
            
         Course.objects.create(
             name = request.POST['name'],
             make_description = makeDescription,
         )
         return redirect('root')

def destroy(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, "destroy.html", context)

def remove(request, id):
    if request.method == 'POST':
       this_course = Course.objects.get(id=id)
       # Manually Delete Description
       if this_course.make_description:
          this_course.make_description.delete()
       #Delete Course
       this_course.delete()
       return redirect('root')