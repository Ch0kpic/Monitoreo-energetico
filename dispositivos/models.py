from django.db import models

# Create your models here.

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