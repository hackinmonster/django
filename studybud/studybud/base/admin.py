from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message


    #we want to be able too view this item and work with it in the admin panel
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)