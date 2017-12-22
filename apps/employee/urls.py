from django.urls import path
from django.conf.urls import url
from django.contrib import admin

# from .views import (
#     # UserCreateAPIView,
#     # UserLoginAPIView
#     )


from . import views


app_name = 'employee'
urlpatterns = [
    # ex: /polls/
    path('',  views.index, name='index'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]