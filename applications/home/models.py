# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible

#import thryparty
from ckeditor.fields import RichTextField

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('nombre', max_length=50, unique=True)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Entry(models.Model):

    title = models.CharField('titulo', max_length=200)
    content = RichTextField('contenido')
    image = models.ImageField(upload_to='blog', verbose_name='imagen')
    created = models.DateField('Fecha de creacion', auto_now_add=True)
    category = models.ManyToManyField(Category, verbose_name='categoria(s)')
    views = models.PositiveIntegerField('visitas', default=0)
    slug = models.SlugField(editable=False)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Entry, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Sugerencia(models.Model):

    title = models.CharField('Titulo', max_length=300)
    contenido = models.TextField(blank=True)
    name = models.CharField('Nombre',max_length=200)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Sugerencia'
        verbose_name_plural = 'Sugerencias'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Subscription(models.Model):
    first_name = models.CharField('nombres', max_length=50, null=True)
    last_name = models.CharField('apellidos', max_length=50, null=True)
    email = models.EmailField('E-mail', max_length=50, unique=True)
    class Meta:
        verbose_name = 'Suscripcion'
        verbose_name_plural = 'Suscripciones'

    def __str__(self):
        return self.first_name


# @python_2_unicode_compatible
# class Contacto(models.Model):
#     name = models.CharField('nombre', max_length=50)
#     email = models.EmailField('E-mail')
#     phone = models.CharField('Telefono', max_length=50)
#     business = models.CharField('Asunto', max_length=50)
#     horario = models.CharField('Sugiera una Hora Para Contactarlo', max_length=50)
#     menssage = models.CharField('¿Cual es tu Consulta?', max_length=200)

#     class Meta:
#         verbose_name = 'Contacto'
#         verbose_name_plural = 'Contactenos'

#     def __str__(self):
#         return self.name
