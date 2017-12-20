from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
        BaseUserManager,
        AbstractBaseUser,
        PermissionsMixin,
        AbstractUser
    )
# from django.contrib.auth.models import PermissionsMixin
# Create your models here.
# Person

# from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


import re
from django import forms
from django.core.exceptions import ValidationError


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class OpUserManager(BaseUserManager):
    def create_user(self, username, mobile, identification, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not mobile:
            raise ValueError('Users must have an mobile address')

        user = self.model(
            username=username,
            mobile=mobile,
            identification=identification,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, mobile,  identification,password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            mobile,
            identification,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class OpUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("用户名"), max_length=255, unique=True)
    identification = models.CharField(_("身份证号"), max_length=100, unique=True)
    mobile = models.CharField(_("手机"),
                              validators=[mobile_validate,],
                              error_messages={'required':u'手机不能为空'} ,
                              max_length=12,
                              unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = OpUserManager()

    USERNAME_FIELD = 'mobile'
    # USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ('username', 'identification',)

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # identification = models.CharField(max_length=100)
    # email = models.EmailField(max_length=255,unique=True)
    # avatar = models.ImageField(_("证件照"), upload_to=avatar_file_name, blank=True)

    def __str__(self):
        return str(self.user.username)