from django.shortcuts import render,redirect, HttpResponse
from .models import Dojo, Ninja

# Create your views here.
def root(request):
    context = {
        'dojos': Dojo.objects.all(),
    }
    return render(request, "index.html", context)


def create_dojo(request):
    if request.method == 'POST':
       Dojo.objects.create(
         name = request.POST['name'],
         city = request.POST['city'],
         state = request.POST['state']
       )
    return redirect("root")

def delete_dojo(request,id):
    Dojo.objects.get(id=id).delete()
    return redirect("root")

def create_ninja(request):
    if request.method == 'POST':
      dojo_id = request.POST['dojo_id']
      
      if dojo_id > 0:
         this_dojo = Dojo.objects.get(id=dojo_id)
         Ninja.objects.create(
             first_name = request.POST['first_name'],
             last_name = request.POST['last_name'],
             dojo = this_dojo
           )

    return redirect("root")