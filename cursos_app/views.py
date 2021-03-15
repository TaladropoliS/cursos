from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Curso, Descripcion, Comentario
from django.db.models import Q, Max, Count, F
# Create your views here.

def inicio(request):
    cursos = Curso.objects.all()
    desc = Descripcion.objects.all()
    context = {
        'cursos':cursos,
        'desc': desc
    }
    return render(request, 'crear.html', context)

def crear(request):
    if request.method == "POST":
        errors = Curso.objects.validador(request.POST)
        if len(errors) > 0:  # si hay errores, recorra cada par clave-valor y cree un mensaje flash
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(inicio)
        else:
            curso = Curso.objects.create(nombre=request.POST['nombre'])
            Descripcion.objects.create(desc=request.POST['desc'], curso=curso)
            return redirect(inicio)
    return redirect(inicio)

def eliminar(request, id):
    curso = Curso.objects.get(id=id)
    context = {
        'curso':curso,
    }
    return render(request, 'eliminar.html', context)

def no_eliminar(request, id):
    return redirect (inicio)

def si_eliminar(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect (inicio)

def comentarios(request, id):
    curso = Curso.objects.get(id=id)
    comentarios = Comentario.objects.filter(curso=Curso.objects.get(id=id))
    if comentarios:
        context = {
            'curso':curso,
            'comentarios':comentarios,
        }
    else:
        no_hay = 'No hay comentarios'
        context = {
            'curso': curso,
            'no_hay': no_hay,
        }
    return render(request, 'comentarios.html', context)

def comentar(request, id):
    if request.method == "POST":
        errors = Curso.objects.validador_coment(request.POST)
        if len(errors) > 0:  # si hay errores, recorra cada par clave-valor y cree un mensaje flash
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/comentarios/{id}')
        else:
            curso = Curso.objects.get(id=id)
            comentario = Comentario.objects.create(coment=request.POST['comentario'], curso=curso)
            return redirect(f'/comentarios/{id}')
    return redirect(f'/comentarios/{id}')