from django.contrib import admin
from .models import GasStorageSolution, GasPipeline, GasApplicationSolution, GasFuelConversion, ValueAddedService, GasProduct

admin.site.register(GasStorageSolution)
admin.site.register(GasPipeline)
admin.site.register(GasApplicationSolution)
admin.site.register(GasFuelConversion)
admin.site.register(ValueAddedService)
admin.site.register(GasProduct)
