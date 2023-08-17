from django.http import HttpResponse
from django.shortcuts import render
from .models import Study


def study(request, id: int):
    try:
        my_study = Study.objects.get(id=id)
        context = {"study": my_study}
        return render("study / study.html", context)
    except Study.DoesNotExist:
        return HttpResponse(f'study {id} does not exist!')
