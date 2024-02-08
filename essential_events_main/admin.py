from django.contrib import admin

from .models import staticModel, menuItems
# Register your models here.
class staticModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']

admin.site.register(staticModel, staticModelAdmin)
admin.site.register(menuItems)