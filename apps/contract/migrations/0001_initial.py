# Generated by Django 2.0rc1 on 2017-12-21 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('0', '有固定期限'), ('1', '无固定期限')], default='0', max_length=10, verbose_name='合同类型')),
                ('start_date', models.DateField(verbose_name='开始时间')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='结束时间')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Company', verbose_name='甲方')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='乙方')),
            ],
            options={
                'verbose_name': '劳动合同',
                'verbose_name_plural': '劳动合同',
            },
        ),
    ]
