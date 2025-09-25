from django.shortcuts import render
from .models import Gallery  # ใช้โมเดล Gallery จริง ๆ

def index(request):
    arts = Gallery.objects.all()  # เปลี่ยนจาก Artwork เป็น Gallery
    return render(request, 'gallery/index.html', {'arts': arts})
