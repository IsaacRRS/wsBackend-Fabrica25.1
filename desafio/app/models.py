from django.db import models



class RegistroModel(models.Model):

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    celular = models.CharField(max_length=30)

    cidade = models.CharField(max_length=50)
    país = models.CharField(max_length=20)

    data = models.DateTimeField(auto_now_add=True)

    def __str__(auto):
        return auto.nome + " " + auto.sobrenome


# ---------------------------------- #


class IPModel(models.Model):

    usuario = models.ForeignKey(RegistroModel, on_delete=models.CASCADE, blank=True, null=True)
    endecIP = models.GenericIPAddressField(unique=True)

    cidade = models.CharField(max_length=100, blank=True, null=True)
    regiao = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    org = models.CharField(max_length=255, blank=True, null=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.endecIP} - {self.cidade}, {self.pais} (Usuário: {self.usuario.nome})"

    
