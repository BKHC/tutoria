from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'avatar/user_{0}.jpg'.format(instance.student.username)

class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=8)
    avatar = models.ImageField(upload_to=user_directory_path)
    wallet = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.student.get_username()
