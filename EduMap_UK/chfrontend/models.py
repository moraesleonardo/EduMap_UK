from django.db import models

<<<<<<< HEAD
class Curso(models.Model):
    DURACAO_CHOICES = [
        ('1', '1 ano'),
        ('2', '2 anos'),
        ('3', '3 anos'),
        ('4', '4 anos'),
        ('5', '5 anos'),
    ]

    CERTIFICADO_CHOICES = [
        ('BSc', 'BSc'),
        ('MSc', 'MSc'),
        ('PhD', 'PhD'),
    ]

    CUSTO_VIDA_CHOICES = [
        ('Alto', 'Alto'),
        ('Médio', 'Médio'),
        ('Baixo', 'Baixo'),
    ]

    AVALIACAO_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100, default='')
    instituicao = models.CharField(max_length=100, default='') 
    duracao = models.CharField(max_length=1, choices=DURACAO_CHOICES)
    tipo_certificado = models.CharField(max_length=10, choices=CERTIFICADO_CHOICES)  # Alteração do tamanho para 10
    custo_de_vida = models.CharField(max_length=10, choices=CUSTO_VIDA_CHOICES)  # Alteração do tamanho para 10
    avaliacao_final = models.IntegerField(choices=AVALIACAO_CHOICES)

    def __str__(self):
        return self.nome
=======
# Create your models here.
>>>>>>> fe5208ff891556a6d785ae0dee2c775a13fb0bed
