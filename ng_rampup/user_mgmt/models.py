from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models

# Create your models here.
# Overriding Default Manager
from django.utils import timezone


class MyManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email, password, first name, last name, level, team, organization.
        """
        now = timezone.now()
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        return self._create_user(email, password, first_name, last_name, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        return self._create_user(email, password, first_name, last_name, True, True,
                                 **extra_fields)


# Overriding Inbuilt User
class MyUser(AbstractUser):
    objects = MyManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __unicode__(self):
        my_user = '%s %s' % (self.get_short_name(), self.email)
        return my_user

MyUser._meta.get_field_by_name('email')[0]._unique = True
MyUser._meta.get_field_by_name('username')[0]._unique = False