from django.contrib import admin

# Register your models here.
from .models import (
    Opuser,
    Profile,
)


admin.site.register(Opuser)
admin.site.register(Profile)
