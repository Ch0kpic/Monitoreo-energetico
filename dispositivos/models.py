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


class Medicion(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='mediciones')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    consumo = models.FloatField(help_text="Consumo en kWh")

    def str(self):
        return f"{self.dispositivo.nombre} - {self.fecha_hora}"


class Alerta(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='alertas')
    medicion = models.ForeignKey(Medicion, on_delete=models.CASCADE, related_name='alertas')
    fecha_hora = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=20, choices=[('advertencia', 'Advertencia'), ('critica', 'Crítica')])
    mensaje = models.TextField()

    def str(self):
        return f"Alerta {self.tipo} - {self.dispositivo.nombre}"
        return f"{self.nombre} ({self.marca} {self.modelo})"
