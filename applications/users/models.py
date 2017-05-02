# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):

        user = self.model(
            username=username,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    TYPE_CHOICES = (
            ('1', 'alumno'),
            ('2', 'docente'),
            ('3', 'Administrador'),
    )
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    username = models.CharField('nombre de usuario', max_length=15, unique=True)
    type_user = models.CharField('tipo de usuario', max_length=2, choices=TYPE_CHOICES, null=True, blank=True)
    first_name = models.CharField('nombres', max_length=50)
    last_name = models.CharField('apellidos', max_length=50)
    avatar = models.URLField(
        'foto',
        blank=True,
    )
    phone = models.CharField('telefono', max_length=50, blank=True, null=True)
    gender = models.CharField('sexo', max_length=1, choices=GENDER_CHOICES)
    date_birth = models.DateField(blank=True, null=True)
    addresse = models.CharField('direccion', max_length=100)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username
