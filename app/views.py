from django.shortcuts import render, redirect

from app.forms import Studyform
from app.models import Study


# Create your views here.
def Study_management(request):
    show = Study.objects.all()
    return render(request, 'Study_management.html', {'show': show})


def Study_View(request, id):
    view = Study.objects.get(id=id)
    return render(request, 'Study_View.html', {'show': view})


def Add_study(request):
    sponsors = Study.objects.values_list('sponsor_name', flat=True).distinct()
    if request.method == 'POST':
        form = Studyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Study_management')
    else:
        form = Studyform()
    return render(request, 'Add_Study.html', {'form': form, 'sponsors': sponsors})


def Study_Edit(request, id):
    view = Study.objects.get(id=id)
    edit = Studyform(instance=view)
    if request.method == 'POST':
        edit = Studyform(request.POST, instance=view)
        if edit.is_valid():
            edit.save()
            return redirect('Study_management')
    return render(request, 'Study_Edit.html', {'edit': edit})


def StudyDelete(request, id):
    delt = Study.objects.get(id=id)
    delt.delete()
    return redirect('Study_management')


def delete_study(request):
    delt = Study.objects.all()
    delt.delete()
    return redirect('Study_management')
