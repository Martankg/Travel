from email.message import Message
from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField( max_length=150, blank=False, verbose_name="Title")
    text = models.TextField( blank=False,verbose_name="Text")
    photo = models.ImageField( upload_to="images/", blank=False ,verbose_name="Photo")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ImageAdd'
        ordering = ['id']

class Contacus(models.Model):
    First_name = models.CharField( max_length=150, blank=False, verbose_name="First Name")
    Second_name = models.CharField( max_length=150, blank=False, verbose_name="Second Name")
    email = models.CharField( max_length=150, blank=False, verbose_name="email")
    mobile = models.IntegerField( verbose_name="Mobile")
    Message = models.TextField( max_length=500, blank=False, verbose_name="Message")
    def __str__(self):
        return self.First_name

    class Meta:
        verbose_name = 'ContacUs'
        ordering = ['id']

    