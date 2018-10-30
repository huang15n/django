from django.shortcuts import render
from django.http import HttpResponse
from .models import Property
from .models import Property_Images
from django.views import generic
"""
def home(request):

    propertyInfo = Property.objects.all()



    images = Property_Images.objects.get(pk=1)
    images_list = images.propertyImages



    return render (request, 'home.html',{'posts' : propertyInfo, 'images':images_list})

"""

class IndexViews(generic.ListView):
    template_name = 'home.html'
    model = Property

    def get_queryset(self):
        return Property.objects.all()









def search(request):
    return render(request, 'search.html')

def contact(request):
    return render(request, 'contact.html')
def registration(request):
    return render(request, 'registration.html')

def advertise(request):
    return  render(request, 'advertise.html')


def about(request):
    return render(request, 'about.html')
def sportequip(request):
    return render(request, 'sportequip.html')

class DetailView(generic.DetailView):
    model = Property
    template_name = 'property_detail.html'
