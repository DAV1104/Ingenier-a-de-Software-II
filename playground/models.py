from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=255)
    nombre_usuario = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=10, choices=[('moderador', 'Moderador'), ('profesor', 'Profesor'), ('estudiante', 'Estudiante')], default='estudiante')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Moderador(models.Model):
    id_moderador = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='moderador')


class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Modulo(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Tema(models.Model):
    id_tema = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    video = models.CharField(max_length=255)
    descripcion = models.TextField()
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)

class Evaluacion(models.Model):
    id_evaluacion = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta = models.TextField()
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)

class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()

class ParticipacionCurso(models.Model):
    id_participacion = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_participacion = models.DateField()
    completado = models.BooleanField()

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    contenido = models.TextField()
    fecha_comentario = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)