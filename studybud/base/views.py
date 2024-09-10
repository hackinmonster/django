from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic
from .forms import RoomForm


#rooms = [
#    {'id':1, 'name':'Lets learn Python'},
#    {'id':2, 'name':'Design with me'},
#    {'id':3, 'name':'Front end Developers'},
#]

def loginPage(request):

    #means user entered their information
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try: #check if user exists
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        #if user exists, make sure credentials are correct, get user object based on username and password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) #log user in
            return redirect('home') #redirect user
        else:
            messages.error(request, 'Username or password does not exist')

    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
                                   
    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)



def room(request, pk): 
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

    #this allows us to pass the room information into the template

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})