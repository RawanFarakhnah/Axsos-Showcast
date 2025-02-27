from django.shortcuts import render, HttpResponse

# Create your views here.
def root(request):
    context = {
        'name': "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, 'index.html', context)