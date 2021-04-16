from django.db import models

from django.contrib.auth.models import User

from PIL import Image

# Create your models here.

class Author (models.Model):
    user_name = models.OneToOneField(User, max_length=20, on_delete=models.CASCADE, related_name='profil')

    bio = models.CharField(max_length=100 , null=True, blank=True)

    city = models.CharField(max_length=20, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    avatar = models.ImageField(blank=True, null=True, upload_to = 'avatars/%Y/%m')

    def __str__(self):
        return self.user_name.username


    def save(self, *args, **kwargs):

        ###IMAGE RESIZE
        super().save(*args,**kwargs)
        if self.avatar: 
            img = Image.open(self.avatar.path)
            if img.height > 400 or img.width > 400:
                output_size = (400,400) 
                img.thumbnail(output_size)
                img.save(self.avatar.path)

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=30)
    
    article = models.CharField(max_length=50)

    creation_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.author)


        






