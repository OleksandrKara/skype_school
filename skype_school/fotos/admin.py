from django.contrib import admin
from skype_school.fotos.models import Foto

class FotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'image_tag', 'date')
    search_fields = ('title', 'date')

admin.site.register(Foto, FotoAdmin)