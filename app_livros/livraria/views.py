from django.shortcuts import redirect, render
from .models import pessoa


def home(request): 
    pessoas = pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def salvar(request):    
    vnome = request.POST.get("nome")
    pessoa.objects.create(nome=vnome)
    pessoas = pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})


def editar(request, id):
    pessoas = pessoa.objects.get(id=id)
    return render(request, "update.html", {"pessoa" : pessoas})


def update(request, id):
    vnome = request.POST.get("nome")
    pessoas = pessoa.objects.get(id=id)
    pessoas.nome = vnome
    pessoas.save()
    return redirect(home)


def delete(request, id):
    pessoas = pessoa.objects.get(id=id)
    pessoas.delete()
    return redirect(home)
