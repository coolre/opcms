from django.contrib import admin

# Register your models here.
from .models import (
    OpUser,
    Profile,
)


admin.site.register(OpUser)
admin.site.register(Profile)
