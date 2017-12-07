from django.contrib import admin

# Register your models here.


from .models import (
    Company,
    Department,
    Project,
)


admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Project)