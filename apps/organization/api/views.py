from django.db.models import Q
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

from apps.organization.models import Company



from .serializers import (
    CompanyListSerializer,
    CompanyDetailSerializer,
    )


class CompanyListAPIView(ListAPIView):
    serializer_class = CompanyListSerializer
    # queryset = Company.objects.all()
    # filter_backends= [SearchFilter, OrderingFilter]
    # permission_classes = [AllowAny]
    # search_fields = ['name']
    # pagination_class = PostPageNumberPagination #PageNumberPagination , *args, **kwargs
    #

    #根据pk列出下属
    def get_queryset(self):
        company_id = self.kwargs.get('pk')
        queryset_list = Company.objects.filter(id=self.kwargs.get('pk')) #filter(user=self.request.user)
        return queryset_list

# 全部
#     def get_queryset(self, *args, **kwargs):
#         queryset = super(CompanyListAPIView, self).get_queryset()
#         return queryset



class CompanyDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = Company.objects.filter(id__gte=0)
    serializer_class = CompanyDetailSerializer
    # permission_classes = [IsOwnerOrReadOnly]


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)