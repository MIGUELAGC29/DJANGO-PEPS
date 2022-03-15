from django.db import models

class Usuario(models.Model):
    SEXO = (
        ('Masculino','Masculino'),
        ('Femenino','Femenino'),
        ('No Binario','No Binario'),
    )
    nombre = models.CharField(max_length=60)
    a_paterno = models.CharField(max_length=60)
    a_Materno = models.CharField(max_length=60)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=60, choices = SEXO, default = 1)
    fecha_nacimiento = models.DateField()