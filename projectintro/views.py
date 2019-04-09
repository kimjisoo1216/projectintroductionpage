from django.shortcuts import render

def intro(request):
    return render(request, 'intro.html')
# Create your views here.
