from django.db import models
from django.conf import settings

# Create your models here.
from apps.contract.models import Contract


User = settings.AUTH_USER_MODEL


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    # contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name=_("甲方"))
    # department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username