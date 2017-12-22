from django.urls import path

from .views import (
    Profile,
    user_create,
    )


app_name = 'accounts'
urlpatterns = [
    # ex: /polls/
    path('',  Profile, name='Profile'),
    path('create/', user_create, name='user_create'),

    # path(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    # path(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # path(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]

