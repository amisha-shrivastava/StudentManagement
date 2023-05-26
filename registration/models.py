from django.db import models

class User(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(choices=(('M', 'Male'), ('F', 'Female')), max_length=1)
    course_preferences = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

