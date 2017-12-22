from django.contrib.auth.decorators import login_required
# from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


from .models import Opuser
from .forms import RegisterForm
# Create your views here.



def Profile(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': 12}
    return render(request, 'accounts/profile.html', context)


# @login_required
def user_create(request):

#     if not request.user.is_staff or not request.user.is_superuser:
#         raise Http404

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        identification = form.cleaned_data['identification']
        mobile = form.cleaned_data['mobile']
        password = form.cleaned_data['password2']
        # MyUser.objects.create_user(username=username, email=email, password=password)
        new_user = Opuser()
        new_user.username = username
        new_user.mobile = mobile
        new_user.identification = identification
        new_user.set_password(password)  # RIGHT
        new_user.save()

    action_url = reverse("accounts:user_create")
    title = "accounts"
    submit_btn = "Create free account"

    context = {
        "form": form,
        "action_url": action_url,
        "title": title,
        "submit_btn": submit_btn
    }
    return render(request, "accounts/user_create.html", context)