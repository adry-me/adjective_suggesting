from django.contrib import admin

# Register your models here.
from .models import Synonym, Adjective


admin.site.register(Synonym)
admin.site.register(Adjective)