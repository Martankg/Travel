from re import search
from django.contrib import admin

# Register your models here.
from .models import *
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'text', 'photo')
    list_display_links = ('id','title')
    # search_fields = ('title')

class ContacusAdmin(admin.ModelAdmin):
    list_display = ('id','First_name', 'Second_name','email','mobile','Message')
    list_display_links = ('id','First_name')
    # search_fields = ('First_name')

admin.site.register(Image, ImageAdmin)
admin.site.register(Contacus, ContacusAdmin)