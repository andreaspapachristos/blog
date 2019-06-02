from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField
from PIL import Image
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 40 or img.width > 40:
            output_size = (40, 40)
            img.thumbnail(output_size)
            img.save(self.image.path)
