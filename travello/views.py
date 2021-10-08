from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'City that never sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 800

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'Biryani first!'
    dest2.img = 'destination_2.jpg'
    dest2.price = 600

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = 'Namma Bengaluru'
    dest3.img = 'destination_3.jpg'
    dest3.price = 400

    dests = [dest1, dest2, dest3]

    return render(request,'index.html', {'dests': dests})