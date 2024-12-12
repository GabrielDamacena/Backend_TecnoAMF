from django.db import models

class Usuario(models.Model):
    foto = models.ImageField(upload_to='fotos_usuarios/', blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    semestre = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.matricula} - {self.cpf}"

class Semestre(models.Model):
    DIAS_DA_SEMANA = [
        ('SEG', 'Segunda-feira'),
        ('TER', 'Terça-feira'),
        ('QUA', 'Quarta-feira'),
        ('QUI', 'Quinta-feira'),
        ('SEX', 'Sexta-feira'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='semestres')
    semestre = models.PositiveIntegerField()
    dia_semana = models.CharField(max_length=3, choices=DIAS_DA_SEMANA)
    cadeira = models.CharField(max_length=100)

    class Meta:
        unique_together = ('usuario', 'semestre', 'dia_semana', 'cadeira')

    def __str__(self):
        return f"{self.usuario.matricula} - Semestre {self.semestre} - {self.get_dia_semana_display()}: {self.cadeira}"
