from django.shortcuts import render

# Create your views here.
def home(request):
    """
    A functional based view for the index page
    """
    return render(request, "index.html")