from django.contrib import admin
from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',) # just to see the created field in admin page


admin.site.register(Todo,TodoAdmin)
