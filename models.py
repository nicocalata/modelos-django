from django.db import models

# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    num = models.IntegerField("Número")
    piso = models.IntegerField(null=True, blank=True)
    depto = models.CharField(max_length=15, null=True, blank=True)
    localidad = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Direcciones"

    def __str__(self):
        return "%s, %s, %s" % (self.localidad, self.calle, self.num)




class TipoMascota(models.Model):
    descripcion = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Tipo de mascota"

    def __str__(self):
        return "%s" % self.descripcion



class Cliente(models.Model):
    num_dni = models.IntegerField("DNI")
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return "%s  %s" % (self.nombre, self.apellido)



class Animal(models.Model):
    nombre = models.CharField("Nombre de la mascota", max_length=25)
    raza = models.CharField(max_length=20)
    tipo_mascota = models.ForeignKey(TipoMascota, on_delete=models.PROTECT, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Animales"

    def __str__(self):
        return "%s,  %s" % (self.nombre, self.cliente.apellido)

        



class Vacuna(models.Model):
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return "%s" % self.descripcion


class MascotaVacuna(models.Model):
    descripcion = models.CharField(max_length=40)
    fecha_vacuna = models.DateField("Fecha Vacuna")
    mascota = models.ForeignKey(Animal, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Mascotas Vacunas"

    def __str__(self):
        return "%s, %s" % (self.fecha_vacuna, self.mascota.nombre)


class Enfermedad(models.Model):
    nombre = models.CharField("Nombre de la enfermedad", max_length=50)
    tipo = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Enfermedades"

    def __str__(self):
        return "%s, %s" % (self.nombre, self.tipo)



class Historial(models.Model):
    se_curo = models.BooleanField("Está sano", default=True)
    mascota = models.ForeignKey(Animal, on_delete=models.PROTECT, null=True, blank=True)
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Historiales"

    def __str__(self):
        return "%s, %s, %s" % (self.se_curo, self.mascota.nombre, self.enfermedad)

class Inyeccion(models.Model):
    descripcion = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Inyecciones"

    def __str__(self):
        return "%s" % self.descripcion


class EnfermedadInyeccion(models.Model):
    fecha_aplicacion = models.DateField("Fecha de aplicacion")
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.PROTECT, null=True, blank=True)
    inyeccion = models.ForeignKey(Inyeccion, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Enfermedades inyecciones"

    def __str__(self):
        return "%s, %s, %s" % (self.fecha_aplicacion, self.enfermedad, self.inyeccion)



class EquiposDiagnostico(models.Model):
    descripcion = models.CharField(max_length=50)

    

    def __str__(self):
        return "%s" % self.descripcion


class Turno(models.Model):
    fecha = models.DateField("Fecha de turno", null=True, blank=True)
    horario = models.TimeField()
    mascota = models.ForeignKey(Animal, on_delete=models.PROTECT, null=True, blank=True)
    equipo_diagnostico = models.ForeignKey(EquiposDiagnostico, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return "%s,%s,%s,%s" % (self.fecha, self.horario, self.mascota, self.equipo_diagnostico)


