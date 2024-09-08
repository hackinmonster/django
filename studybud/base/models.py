from django.db import models
from django.contrib.auth.models import User
    #django has buillt in user model


        #once we add a model, we need to make migrations
        #python manage.py makemigrations
        #python manage.py migrate

# Create your models here.



class Topic(models.Model):
    #one to many relationship, topic can have multiple rooms
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
        #null=True means the database can have an instance of this model without a description value
    description = models.TextField(null=True, blank=True)
    #participants = 
        #every time the save method is called, add a timestamp
    updated = models.DateTimeField(auto_now=True)
        #auto_now takes snapshot every time we save
        #auto_now_add only takes a snapshot the first time we save
    created = models.DateTimeField(auto_now_add=True)

    class Meta: #order by descending date, newest first
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    

    
class Message(models.Model):
    #one to many relationship, user can have many messages
    user = models.ForeignKey(User, on_delete=models.CASCADE)
        #when parent is deleted, what do we do with children?
        #set null or cascade
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]



