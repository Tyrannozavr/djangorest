from django.contrib import admin

from .models import Message, Tickets

admin.site.register(Tickets)
admin.site.register(Message)
# Register your models here.
