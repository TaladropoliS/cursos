from __future__ import unicode_literals
from django.db import models

# Create your models here.

class FormManager(models.Manager):
    def validador(self, postData):
        errors = {}
        if len(postData['nombre']) < 5:
            errors["nombre"] = "Ingresar nombre."
        if len(postData['desc']) < 15:
            errors["desc"] = "Ingresar descripción."
            return errors
        return errors
    def validador_coment(self, postData):
        errors = {}
        if len(postData['comentario']) < 3:
            errors["comentario"] = "Ingresar comentaroio con más de 3 caracteres."
            return errors
        return errors

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FormManager()

class Descripcion(models.Model):
    desc = models.TextField()
    curso = models.OneToOneField (Curso, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FormManager()

class Comentario(models.Model):
    coment = models.TextField()
    curso = models.ForeignKey(Curso, related_name="comentarios", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FormManager()