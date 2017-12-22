from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def Profile(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': 12}
    return render(request, 'accounts/profile.html', context)


@login_required
def job_add(request):
    pass


	# title = "Add Job"
	# job = UserJob.objects.all()[0]
	# form = UserJobForm(request.POST or None)
	# if form.is_valid():
	# 	instance = form.save(commit=False)
	# 	instance.user = request.user
	# 	instance.save()
	# 	return redirect("profile_user")
	# context = {
	# 	"form": form,
	# 	"title": title,
	# 			}
	# return render(request, "forms.html", context)