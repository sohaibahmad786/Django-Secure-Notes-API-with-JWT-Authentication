from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Register
from .models import Note

admin.site.register(Note)
admin.site.register(Register,UserAdmin)
# Register your models here.
