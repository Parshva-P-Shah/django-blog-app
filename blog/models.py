from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='photo/')
    STATUS_CHOICE=(
        ('public','Public'),
        ('private','Private')
    )
    status=models.CharField(max_length=10,choices=STATUS_CHOICE,default='public')

    def __str__(self):
        return f'{self.user.username} - {self.content[:10]}'


