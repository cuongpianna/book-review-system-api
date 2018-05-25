from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    GENDER = (
        ('M','Nam'),
        ('F','Nữ'),
        ('O','Khác'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    gender = models.CharField(max_length=5,choices=GENDER,default='M')
    date_of_birth = models.DateField(blank=True,null=True)

    def __str__(self):
        return 'Profile cua {}'.format(self.user.username)

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            profile = Profile(user=instance)
            profile.save()

