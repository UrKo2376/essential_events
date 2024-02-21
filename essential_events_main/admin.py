from django.contrib import admin

from .models import staticModel, menuItems, actsModel, actImages
# Register your models here.
class staticModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image']

admin.site.register(staticModel, staticModelAdmin)
admin.site.register(menuItems)
admin.site.register(actsModel)
admin.site.register(actImages)