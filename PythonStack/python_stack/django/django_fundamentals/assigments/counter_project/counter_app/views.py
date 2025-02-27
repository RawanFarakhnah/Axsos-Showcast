from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def root(request):
    if "counter" not in request.session: 
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    return render(request, "index.html")

def increase(request):
    request.session['counter'] = request.session.get('counter', 0) + 2
    return redirect(reverse('index')) #as url_for()

def custom_increase(request):
    if request.method == 'POST':
       custom_counter = request.POST['custom_counter']
       request.session['counter'] = request.session.get('counter', 0) + int(custom_counter)
       return redirect(reverse('index'))


def clear_session(request):
    request.session.flush()
    return redirect(reverse('index'))