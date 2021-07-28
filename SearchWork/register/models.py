from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)


class Employees(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    birth_day = models.DateField()

    def __str__(self):
        return f"{self.username}"


class Category(models.Model):
    CATEGORY = ('Administrative', 'Administrative'
                'Manager', 'Manager')
    name = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128, unique=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.URLField()
    views = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"{self.category.name} - {self.title} - {self.views}"


class Employer(models.Model):
    company_name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=10000)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()