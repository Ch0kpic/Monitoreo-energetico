from django.contrib import admin
from .models import Categoria, Zona, Dispositivo, Medicion, Alerta

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'modelo', 'potencia_nominal', 'estado', 'categoria', 'zona')
    list_filter = ('estado', 'categoria', 'zona')

@admin.register(Medicion)
class MedicionAdmin(admin.ModelAdmin):
    list_display = ('dispositivo', 'fecha_hora', 'consumo')
    list_filter = ('dispositivo',)

@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ('dispositivo', 'medicion', 'fecha_hora', 'tipo', 'mensaje')
    list_filter = ('tipo', 'dispositivo')

