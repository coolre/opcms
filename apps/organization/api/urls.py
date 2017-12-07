from django.urls import path
from django.contrib import admin

from .views import (
    CompanyDetailAPIView,
    CompanyListAPIView,

)

# urlpatterns = [
#     path(r'^$', CommentListAPIView.as_view(), name='list'),
#     path(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
#     path(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
#     # url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
# ]

app_name = 'organization-api'
urlpatterns = [
    path('', CompanyListAPIView.as_view(), name='list'),
    path('<int:pk>/', CompanyDetailAPIView.as_view(), name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]