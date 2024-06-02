from django.contrib import admin

from .models import AdditionMaterial, Topic, Module, Program

# Register models.
admin.site.register(AdditionMaterial)
admin.site.register(Topic)
admin.site.register(Module)
admin.site.register(Program)
