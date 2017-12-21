from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from apps.organization.models import Company

User = settings.AUTH_USER_MODEL

TYPE_CHOICES = (
    ('0', '有固定期限'),
    ('1', '无固定期限'),
)


# Create your models here.
class Contract(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("乙方"))
    employer = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_("甲方"))
    type = models.CharField(_('合同类型'), max_length=10, choices=TYPE_CHOICES, default='0')
    start_date = models.DateField(_("开始时间"))
    end_date = models.DateField(_("结束时间"), blank=True, null=True)
    # photo = models.ForeignKey(Certificate, on_delete=models.CASCADE, verbose_name=_("合同扫描件"), blank=True, null=True)

    class Meta:
        verbose_name = _('劳动合同')
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % self.person