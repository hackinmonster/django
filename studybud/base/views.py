from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id':1, 'name':'Lets learn Python'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Front end Developers'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk): 
    room = None
    #loop through list of rooms, whatever room id matches the pk from the url, get that room
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)

    #this allows us to pass the room information into the template
