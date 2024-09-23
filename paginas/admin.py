from django.contrib import admin
from paginas.models import Flan, Contact


class FlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Flan, FlanAdmin)

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)