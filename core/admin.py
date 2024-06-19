from django.contrib import admin

from .models import Persona, Carro, Pago, Logcarro

admin.site.register(Persona)
admin.site.register(Carro)
admin.site.register(Pago)
admin.site.register(Logcarro)
