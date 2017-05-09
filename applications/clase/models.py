# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.db import models
# from django.conf import settings

# # Create your models here.


# class Docente(models.Model):
# 	"""modelo que representa un docente"""
# 	epecialidad = models.CharField('nombre', max_length=200)
# 	experiencia = models.PositiveIntegerField(default=2)
# 	user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         related_name="usuario_docente",
#     )

# 	class Meta:
#         verbose_name = 'Docente'
#         verbose_name_plural = 'Docentes'

#     def __str__(self):
#         return self.name