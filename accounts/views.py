from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Profile(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': 12}
    return render(request, 'profile.html', context)