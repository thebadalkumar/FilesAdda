from django.db import models
from django.contrib.auth.models import User
from .utils import create_shortened_url
import os
# Create your models here.

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False


def custom_path(instance, filename):
    return 'user_{}/{}'.format(instance.user.id, filename)

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=custom_path)
    title = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=15, unique=True, blank=True)
    is_delete = models.BooleanField(default=False)
    is_fav = models.BooleanField(default=False)
    def __str__(self):
        return str(self.file).split("/")[-1]
    
    def css_class(self):
        name, extension = os.path.splitext(self.file.name)
        if extension == '.pdf':
            return 'pdf'
        if extension == '.txt' or extension == ".ini":
            return 'text'
        if extension == '.py':
            return 'python'
        if extension == '.js':
            return 'javascript'
        if extension == '.html' or extension == '.htm' or extension == '.xml':
            return 'html'
        if extension == '.doc' or extension == '.docx':
            return 'word'
        if extension == '.xls' or extension == '.xlsx':
            return 'excel'
        if extension == '.png' or extension == '.jpg' or extension == ".jpeg" or extension == ".gif" or extension == ".bmp":
            return 'image'
        if extension == '.mp3' or extension == '.wav':
            return 'music'
        return 'other'

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = create_shortened_url(self)
        super().save(*args, **kwargs)