from django.shortcuts import render,redirect
from .models import *
from .forms import*
# Create your views here.
def index(req):
    return render(req, 'index.html')

def spisok(req):
    bd = Kino.objects.all()
    data = {'kinobase': bd}
    return render(req, 'spisok.html', context=data)

def country(req):
    forma = Kinofilmcountry()
    data = {'forma': forma}
    return render(req, 'country.html', context=data)

def countryfilter(req):
    print(1)
    if Kinofilmcountry(req.POST):
        print(2)
        k1 = req.POST.get('country1')
        bd = Kino.objects.filter(country=k1)
        data = {'kinobase': bd}
        print(bd)
        return render(req, 'countryfilter.html', context=data)
    else:
        print(3)
        kn = Kinofilmcountry()
        data = {'form':kn}
        return render(req, 'country.html',context=data)

def year(req):
    forma = Kinofilmyear()
    data = {'forma': forma}
    return render(req, 'year.html', context=data)

def yearfilter(req):
    print(4)
    if Kinofilmyear(req.POST):
        print(5)
        k1 = req.POST.get('year1')
        bd = Kino.objects.filter(year=k1)
        data = {'kinobase': bd}
        print(bd)
        return render(req, 'yearfilter.html', context=data)
    else:
        print(6)
        kn = Kinofilmyear()
        data = {'form':kn}
        return render(req, 'year.html',context=data)

def noyear(req):
    forma = Kinofilmnoyear()
    data = {'forma': forma}
    return render(req, 'noyear.html', context=data)

def noyearfilter(req):
    print(7)
    if Kinofilmyear(req.POST):
        print(8)
        k1 = req.POST.get('year1')
        bd = Kino.objects.exclude(year=k1)
        data = {'kinobase': bd}
        print(bd)
        return render(req, 'spisok.html', context=data)
    else:
        print(9)
        kn = Kinofilmyear()
        data = {'form': kn}
        return render(req, 'noyear.html', context=data)