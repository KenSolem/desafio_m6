from django.contrib import admin
from paginas.models import Flan


class FlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Flan, FlanAdmin)