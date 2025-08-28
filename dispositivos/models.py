from django.db import models

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="dispositivos")
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name="dispositivos")
    consumo_maximo = models.IntegerField(default=100)  # límite por defecto
