from django.db import models
from django.urls import reverse

# Create your models here.


class CompanyManager(models.Manager):
    def all(self):
        qs = super(CompanyManager, self).filter(parent=None)
        return qs

    # def filter_by_instance(self, instance):
    #     content_type = ContentType.objects.get_for_model(instance.__class__)
    #     obj_id = instance.id
    #     qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
    #     return qs


class Company(models.Model):
    title = models.CharField(max_length=500)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    objects = CompanyManager()

    def __str__(self):
        return self.title

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
    name = models.CharField(max_length=500)


class Project(models.Model):
    name = models.CharField(max_length=500)

