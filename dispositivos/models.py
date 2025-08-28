from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def str(self):
        return self.nombre
    
class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def str(self):
        return self.nombre
    
class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    potencia_nominal = models.FloatField(help_text="Potencia en W")
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='dispositivos')
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='dispositivos')

    def str(self):
        return f"{self.nombre} ({self.marca} {self.modelo})"