# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Secretaria(models.Model):

    #__Secretaria_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Secretaria_FIELDS__END

    class Meta:
        verbose_name        = _("Secretaria")
        verbose_name_plural = _("Secretaria")


class Dispositivo(models.Model):

    #__Dispositivo_FIELDS__
    secretaria_id = models.ForeignKey(secretaria, on_delete=models.CASCADE)
    setor_id = models.ForeignKey(setor, on_delete=models.CASCADE)

    #__Dispositivo_FIELDS__END

    class Meta:
        verbose_name        = _("Dispositivo")
        verbose_name_plural = _("Dispositivo")


class Setor(models.Model):

    #__Setor_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    secretaria_id = models.ForeignKey(secretaria, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Setor_FIELDS__END

    class Meta:
        verbose_name        = _("Setor")
        verbose_name_plural = _("Setor")



#__MODELS__END
