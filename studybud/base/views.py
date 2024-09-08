from django.shortcuts import render
from .models import Room

#rooms = [
#    {'id':1, 'name':'Lets learn Python'},
#    {'id':2, 'name':'Design with me'},
#    {'id':3, 'name':'Front end Developers'},
#]

def home(request):
    
    rooms = Room.objects.all #give us all the rooms in db, overriding variable initialized above
    context = {'rooms': rooms}
    return render(request, 'base/home.html', {'rooms': rooms})



def room(request, pk): 
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

    #this allows us to pass the room information into the template
