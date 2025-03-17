from django.shortcuts import render, redirect
from .models import Show, ShowManager
from django.contrib import messages

# Create your views here.
#Main Show rout
def root(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, "root.html", context)

#view Show information
def view_show(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "view_show.html", context)


#Add New Show 
def new_show(request):
    if request.method == "GET":
       return render(request, "create.html")
    
def create_show(request):
    if request.method == "POST":
       errors = Show.objects.basic_validator(request.POST)
       if len(errors) > 0:
          for key, value in errors.items():
              messages.error(request, value)
          return redirect('new_show')
       else: 
          Show.objects.create(
              title = request.POST['title'],
              network = request.POST['network'],
              release_date = request.POST['release_date'],
              description = request.POST['description']
          )
          return redirect('root')
       
def edit_show(request, id):
    show = Show.objects.get(id=id)
    if show.release_date:
        show.release_date = show.release_date.strftime('%Y-%m-%d')

    context = {"show": show}
    return render(request, "edit.html", context)

def update_show(request, id):
    if request.method == "POST":
       errors = Show.objects.basic_validator(request.POST)
       if len(errors) > 0:
          for key, value in errors.items():
              messages.error(request, value)
          return redirect('edit_show', id=id)
       else: 
          show = Show.objects.get(id=id)
          show.title = request.POST['title']
          show.network = request.POST['network']
          show.release_date = request.POST['release_date']
          show.description = request.POST['description']
          show.save()
          return redirect('view_show', id=id)
       
def delete_show(request, id):
     Show.objects.get(id=id).delete()
     return redirect('root')
