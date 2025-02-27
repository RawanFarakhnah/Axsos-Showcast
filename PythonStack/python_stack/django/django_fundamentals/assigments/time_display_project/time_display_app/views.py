from django.shortcuts import render,redirect
from datetime import datetime
from time import gmtime, localtime, strftime

# Create your views here.

def root(request):
    return redirect('/time_display')


def time_display(request):
    #gmtime() → Returns UTC time (which might not match your local time).
    #localtime() → Returns the time in your system's local time zone.

    context = {
       'current_time': strftime("%b %d, %Y %I:%M %p", localtime())
        # 'current_time': strftime("%b %d, %Y %I:%M %p", gmtime())
        # 'current_time': datetime.now().strftime("%b %d, %Y %I:%M %p")
    }

    return render(request,'index.html', context )
