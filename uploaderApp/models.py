from django.db import models
from django.contrib.auth.models import User
from django.forms import FileField
from .utils import create_shortened_url
# Create your models here.
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

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = create_shortened_url(self)
        super().save(*args, **kwargs)