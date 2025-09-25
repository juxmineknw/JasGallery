from django.shortcuts import render
from .models import Artwork

def index(request):
    arts = Artwork.objects.all()
    return render(request, 'gallery/index.html', {'arts': arts})
