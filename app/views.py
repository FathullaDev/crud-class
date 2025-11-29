from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *

from app.forms import *
from app.models import *
def index(request):
    otm = Otm.objects.all()
    return render(request, 'index.html', {'otm': otm})

def groups_by_otm(request, otm_id):
    selected_otm = get_object_or_404(Otm, id=otm_id)
    all_otm = Otm.objects.all()
    groups_for_selected = Groups.objects.filter(otm_id=otm_id)

    return render(request, 'groups.html', {
        'selected_otm': selected_otm,
        'all_otm': all_otm,
        'groups_for_selected': groups_for_selected,
    })


def students_by_groups_and_otm(request, otm_id, group_id):
    otm = get_object_or_404(Otm, id=otm_id)
    group = get_object_or_404(Groups, id=group_id, otm_id=otm_id)
    students = Students.objects.filter(group=group).order_by('id')
    all_otm = Otm.objects.all()
    return render(request, 'students.html',{
        'otm': otm,
        'group': group,
        'students': students,
        'all_otm': all_otm,
    })

def view_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    return render(request, 'view_student.html', {'student': student})


#add functions
def add_otm(request):
    if request.method=='POST':
        form=OtmForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=OtmForm()
    return render(request,'add_otm.html',{'form':form})

def add_group(request):
    if request.method=='POST':
        form=GroupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=GroupForm()
    return render(request,'add_group.html',{'form':form})

def add_student(request):
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=StudentForm()
    return render(request,'add_student.html',{'form':form})


#update functions
def update_otm(request,otm_id):
    otm=get_object_or_404(Otm,pk=otm_id)

    if request.method=='POST':
        form=OtmForm(request.POST,instance=otm)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=OtmForm(instance=otm)

    return render(request,'update_otm.html',{'form': form, 'otm': otm})


def update_group(request,group_id):
    group = get_object_or_404(Groups, pk=group_id)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GroupForm(instance=group)

    return render(request, 'update_group.html',{'form': form, 'group': group})


def update_student(request,student_id):
    student = get_object_or_404(Students, pk=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {'form': form, 'student': student})



# #delete functions
def delete_otm(request,otm_id):
    otm=get_object_or_404(Otm,pk=otm_id)
    otm.delete()
    return redirect('home')

def delete_group(request,group_id):
    group=get_object_or_404(Groups,pk=group_id)
    group.delete()
    return redirect('home')

def delete_student(request,student_id):
    student=get_object_or_404(Students,pk=student_id)
    student.delete()
    return redirect('home')