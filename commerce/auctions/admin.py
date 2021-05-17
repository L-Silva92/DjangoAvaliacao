from django.contrib import admin
from .models import categ, leilao, User
class leilaoadmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "descricao", "valor_min", "catego", "dono")

# Register your models here.
admin.site.register(categ)
admin.site.register(leilao, leilaoadmin)
admin.site.register(User)