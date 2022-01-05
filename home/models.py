from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields import TextField

# Create your models here.

class categorie(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f'{self.name}' 

class child_cate(models.Model):
    name = models.CharField(max_length=200)
    slug_child = models.SlugField(unique=True)
    datetime = models.DateField(auto_now_add=True)
    categorie_child = models.ForeignKey(categorie,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class content_home(models.Model):
    title = models.CharField(max_length=200)
    description = TextField(max_length=300)
    content = RichTextUploadingField(blank=True,null=True)
    image = models.ImageField(upload_to='images')
    datetime = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    categories = models.ForeignKey(child_cate,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.author} - {self.datetime}'

