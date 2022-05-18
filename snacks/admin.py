from django.contrib import admin
from .models import snack

# Register your models here.

@admin.register(snack)
class AdminSnack(admin.ModelAdmin):
    list_display = ["id",'title',"purshaser","description"]
    search_fields = ('title',)

