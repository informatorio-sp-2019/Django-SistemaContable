from django.contrib import admin
from cuentas import models
# Register your models here.
class MovimientoAdmin(admin.ModelAdmin):
	pass

class CuentaAdmin(admin.ModelAdmin):
	pass
	
class LocalidadAdmin(admin.ModelAdmin):
	pass

admin.site.register(models.Localidad, LocalidadAdmin)
admin.site.register(models.Cuenta, CuentaAdmin)
admin.site.register(models.Movimiento, MovimientoAdmin)