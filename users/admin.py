from django.contrib import admin

from users.models import User, UserGroup

# Register models.
admin.site.register(User)
admin.site.register(UserGroup)
