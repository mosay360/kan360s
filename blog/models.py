from distutils.command.upload import upload
from email.policy import default
from pickle import TRUE
#from turtle import update
from unicodedata import category, name
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User;
from taggit.managers import TaggableManager
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:blogIndex')
    
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories' 




class PublishedManager(models.Manager):
    
 def get_queryset(self):
  return super(PublishedManager,self).get_queryset().filter(status='published')
    


class Post(models.Model):


    STATUS_CHOICES= (
       ('draft', 'Draft'),
       ('published', 'Published') ,
    )
    title =models.CharField(max_length=250)
    tags = TaggableManager()
   
    slug= models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category= models.CharField(max_length=250, default="Hello")
    blogImage= models.ImageField(upload_to ='blogImages', null=True, blank= True,)
    body = RichTextField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering= ('-publish',)
        
    def __str__(self):
        return self.title  


    def get_absolute_url(self):
        return reverse('blog:postDetail',args=
        [self.publish.year,
        self.publish.month, self.publish.day, self.slug])
    

def get_absolute_url(self):
        return reverse('blob:blogIndex')


        
class Comment(models.Model):
    post = models.ForeignKey(Post,
    on_delete=models.CASCADE,
    related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    def __str__(self):
     return f'Comment by {self.name} on {self.post}'

    
class Slider(models.Model):
    slideImage= models.ImageField(upload_to = 'sliderPics')
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    body = RichTextField(blank= TRUE, null= TRUE)