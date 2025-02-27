from django.shortcuts import render

# Create your views here.
def root(request):
   return render(request, "index.html")

def viewResult(request):
   formOutput = request.POST
   selected_communications = request.POST.getlist("communication")
   selected_satisfaction = request.POST.getlist("satisfaction")
   context = {
      'formOutput' : formOutput,
      'selected_communications': selected_communications,
      'selected_satisfaction': selected_satisfaction
   }
   return render(request, "view.html", context)
  