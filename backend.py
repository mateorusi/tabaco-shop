# models.py
from django.db import models

class Produkt(models.Model):
    emri = models.CharField(max_length=255)
    pershkrimi = models.TextField()
    cmimi = models.DecimalField(max_digits=10, decimal_places=2)
    sasija = models.IntegerField()
    foto = models.ImageField(upload_to='produkte/')
    kategoria = models.CharField(max_length=100)

    def __str__(self):
        return self.emri

# models.py
from django.db import models

class Produkt(models.Model):
    emri = models.CharField(max_length=255)
    pershkrimi = models.TextField()
    cmimi = models.DecimalField(max_digits=10, decimal_places=2)
    sasija = models.IntegerField()
    foto = models.ImageField(upload_to='produkte/')
    kategoria = models.CharField(max_length=100)

    def __str__(self):
        return self.emri

# views.py
from django.shortcuts import render, redirect
from .forms import ProduktForm

def shto_produkt(request):
    if request.method == 'POST':
        form = ProduktForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_produkteve')  # Redirect në listën e produkteve
    else:
        form = ProduktForm()
    return render(request, 'shto_produkt.html', {'form': form})
# forms.py
from django import forms
from .models import Produkt

class ProduktForm(forms.ModelForm):
    class Meta:
        model = Produkt
        fields = ['emri', 'pershkrimi', 'cmimi', 'sasija', 'foto', 'kategoria']

# views.py
from django.shortcuts import render
from .models import Produkt

def lista_produkteve(request):
    produktet = Produkt.objects.all()
    return render(request, 'lista_produkteve.html', {'produktet': produktet})
# views.py
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProduktForm
from .models import Produkt

def perditeso_produkt(request, produkt_id):
    produkt = get_object_or_404(Produkt, id=produkt_id)
    if request.method == 'POST':
        form = ProduktForm(request.POST, request.FILES, instance=produkt)
        if form.is_valid():
            form.save()
            return redirect('lista_produkteve')
    else:
        form = ProduktForm(instance=produkt)
    return render(request, 'perditeso_produkt.html', {'form': form})
