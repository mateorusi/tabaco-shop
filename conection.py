# emri_aplikacionit/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# emri_aplikacionit/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),  # Lidh me view-n 'index'
]

# emri_projektit/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),  # Përcakto rrugën për aplikacionin tënd
]
