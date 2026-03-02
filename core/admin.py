from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Property, Message

# Register your models here.
@admin.register(Property)
class PropertyAdmin(ModelAdmin):
    list_display = ['title', 'location', 'price', 'status']

@admin.register(Message)
class MessaAdmin(ModelAdmin):
    readonly_fields = ['name', 'email', 'message']
    