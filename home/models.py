from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pic = models.ImageField(default="default.png",upload_to='profilepic')
    bio = models.CharField(max_length=500)
    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.pic.path)
    #
    #     if img.height> 300 or img.width > 300:
    #         output_size =(300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.pic.path)

class post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    about=models.CharField(max_length=300)
    image=models.ImageField(upload_to='post')

    def __str__(self):
        return f'{self.user.username} post'