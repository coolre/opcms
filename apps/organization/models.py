from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class CompanyManager(models.Manager):
    def all(self):
        qs = super(CompanyManager, self).filter(parent=None)
        return qs

    # def filter_by_instance(self, instance):
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     obj_id = instance.id
    #     qs = super(CompanyManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
    #     return qs


class Company(models.Model):
    title = models.CharField(max_length=500)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')

    objects = CompanyManager()

    def __str__(self):
        return self.title
        # if self.parent is not None:
        #     return ' - '.join((self.title, self.pk))
        # else:
        #     return self.title

    def get_absolute_url(self):  # get_absolute_url
        # return f"/restaurants/{self.slug}"
        return reverse('detail', kwargs={'slug': self.slug})

    # def children(self):  # replies
    #     return Company.objects.filter(parent=self)

    def get_child(self):
        if self.is_child:
            return None
        else:
            return Company.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    @property
    def is_child(self):
        if self.parent is not None:
            return True
        else:
            return False


class Department(models.Model):
    title = models.CharField(max_length=500)


class Project(models.Model):
    title = models.CharField(max_length=500)

class ProjectDepartment(models.Model):
    title = models.CharField(max_length=500)

