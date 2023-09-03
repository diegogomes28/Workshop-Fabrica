from django.db import models
##CRIAÇÃO Do MOdel Pessoa(funcionario)
class pessoa(models.Model):
    nome = models.CharField(max_length=100) #limite de caracteres
    
    def __str__(self): #não reconhecer como obj
        return self.nome