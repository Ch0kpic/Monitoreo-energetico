from django.shortcuts import render
from .models import Dispositivo, Medicion, Alerta

def panel(request):
    dispositivos = Dispositivo.objects.all()
    alertas = Alerta.objects.order_by('-fecha_hora')[:10]  # últimas 10 alertas
    return render(request, 'dispositivos/panel.html', {
        'dispositivos': dispositivos,
        'alertas': alertas
    })