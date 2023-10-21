from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Study


def study(request, study_id: int):
    try:
        my_study = Study.objects.get(id=study_id)
        context = {"study": my_study}
        return render(request, "study/study.html", context=context)
    except Study.DoesNotExist:
        return HttpResponse(f'study {study_id} does not exist!')

# def study(request, study_id: int):
#     my_study = Study.objects.get(id=study_id)
#     context = {"study": my_study}
#     return render(request, "study/study.html", context=context)


# def study(request, study_id: int):
#     if not request.user.is_authenticated:
#         return redirect('home')
#
#
# @login_required()
# def study(request, study_id: int):
#     ...


def signup(request, study_id: int):
    return HttpResponse(f'Not implemented yet!')
