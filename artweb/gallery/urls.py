from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gallery_list'),   # ใช้ views.index แทน
    # path('<int:pk>/', views.gallery_detail, name='gallery_detail'), 
    # ถ้ายังไม่มี gallery_detail ให้คอมเมนต์ไว้ก่อน
]