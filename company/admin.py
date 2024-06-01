from django.contrib import admin

from .models import Organization, Department, Position, Worker

# Register models.
admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Worker)