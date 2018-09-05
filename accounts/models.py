from django.db import models
from django.contrib.auth.models import AbstractUser

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class User(AbstractUser):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    
    is_writer = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    topic_of_interest = models.CharField(max_length=150, null=True)
    resume = models.ImageField(upload_to=user_directory_path, null=True)
    full_name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return str(self.pk)


