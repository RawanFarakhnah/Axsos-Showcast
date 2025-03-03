from django.shortcuts import render, redirect
from  random import randrange
from django.urls import reverse

# Create your views here.
def root(request):
    if 'random' not in request.session:
       request.session['random'] = randrange(1, 101)
       request.session['attempts'] = 0 
       request.session['success'] = False
       request.session['message'] = ''
 
    context = {
        'success': request.session.get('success', False), 
        'message': request.session.get('message', '')
        }
    
    print("session['random']", request.session['random'])
    return render(request, 'index.html', context)

def try_again(request):
    request.session.flush()
    return redirect(reverse('root'))


def guess_number(request):
    if request.method == 'POST':
       guess = int(request.POST['guess_number'])
       request.session['attempts'] += 1

       if guess == request.session['random']:
           request.session['success'] = True
       elif guess < request.session['random']:
           request.session['success'] = False
           request.session['message'] = 'Too Low!'
       else:
           request.session['success'] = False
           request.session['message'] = 'Too High!'
       
       request.session.modified = True
       return redirect(reverse('root'))