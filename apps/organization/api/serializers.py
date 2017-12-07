from apps.organization.models import Company

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

# from apps.accounts import UserDetailSerializer
#
# User = get_user_model()

#
# class CompanySerializer(ModelSerializer):
#     sub_count = SerializerMethodField()
#
#     class Meta:
#         model = Company
#         fields = [
#             'id',
#             'name',
#             'parent',
#             'sub_count',
#         ]
#
#     def get_sub_count(self, obj):
#         if obj.is_parent:
#             return obj.children().count()
#         return 0


class CompanyListSerializer(ModelSerializer):
    # url = HyperlinkedIdentityField(
    #     view_name='list',
    #     lookup_field='id')
    sub_count = SerializerMethodField()
    children = SerializerMethodField()

    class Meta:
        model = Company
        fields = [
            # 'url',
            'id',
            'name',
            # 'object_id',
            'parent',
            # 'content',
            'sub_count',
            'children',
        ]

    def get_sub_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    def get_children(self, obj):
        if obj.is_parent:
            return CompanyChildSerializer(obj.children(), many=True).data
        return None


class CompanyChildSerializer(ModelSerializer):
    # user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Company
        fields = [
            'id',
            # 'user',
            'name',
            # 'timestamp',
        ]


class CompanyDetailSerializer(ModelSerializer):
    # user = UserDetailSerializer(read_only=True)
    sub_count = SerializerMethodField()
    # content_object_url = SerializerMethodField()
    sub = SerializerMethodField()

    class Meta:
        model = Company
        fields = [
            'id',
            # 'user',
            # 'content_type',
            # 'object_id',
            'name',
            'sub_count',
            'sub',
            # 'timestamp',
            # 'content_object_url',
        ]
        read_only_fields = [
            # 'content_type',
            # 'object_id',
            'sub_count',
            # 'replies',
        ]

    # def get_content_object_url(self, obj):
    #     try:
    #         return obj.content_object.get_api_url()
    #     except:
    #         return None

    def get_sub(self, obj):
        if obj.is_parent:
            return CompanyChildSerializer(obj.children(), many=True).data
        return None

    def get_sub_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0