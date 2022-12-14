from django.contrib import admin
from django_seminario_app.models import Inscripcion
# Register your models here.

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut']

admin.site.register(Inscripcion, InscripcionAdmin)
