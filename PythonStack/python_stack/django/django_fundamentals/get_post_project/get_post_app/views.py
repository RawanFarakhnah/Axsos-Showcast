from django.shortcuts import render, redirect, HttpResponse

# Root view: Clears session and shows default values
def root(request):
    request.session.flush()  # Completely clears session on first visit
    # request.session.setdefault('user_data', {}) 
    
    # if 'username' in request.session:
    #     del request.session['username']  # Deletes only the 'username' session key

    if request.method == "GET":
       return render(request, 'some_template.html')

    if request.method == "POST":
        return redirect('/')
   

# Function to handle form submission & set session data
def some_function(request):
    if request.method == "POST":
        # Store user input in session, using get() to prevent errors
        request.session['username'] = request.POST.get('username', 'Guest')
        request.session['email'] = request.POST.get('email', 'Not Provided')
        request.session.modified = True  # Ensures session updates

        return redirect('/success')

    return HttpResponse("Invalid Request", status=400)  # Handle other methods

# Success route: Display session data safely
def show_user(request):
    context = {
        'username': request.session.get('username', 'Guest'),
        'email': request.session.get('email', 'Not Provided')
    }
    return render(request, 'show.html', context)
