from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from app.forms import *
from app.models import *
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)


def index(request):
    otm = Otm.objects.all()
    return render(request, 'index.html', {'otm': otm})

class OtmListView(ListView):
    model = Otm
    template_name = 'index.html'
    context_object_name = 'otm'



def groups_by_otm(request, otm_id):
    selected_otm = get_object_or_404(Otm, id=otm_id)
    all_otm = Otm.objects.all()
    groups_for_selected = Groups.objects.filter(otm_id=otm_id)

    return render(request, 'groups.html', {
        'selected_otm': selected_otm,
        'all_otm': all_otm,
        'groups_for_selected': groups_for_selected,
    })

class GroupsByOtmView(ListView):
    model = Otm
    template_name = 'groups.html'
    context_object_name = 'all_otm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        otm_id = self.kwargs['otm_id']

        context['selected_otm'] = get_object_or_404(Otm, id=otm_id)
        context['groups_for_selected'] = Groups.objects.filter(otm_id=otm_id)
        return context


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

class StudentsByGroupAndOtmView(ListView):
    model = Students
    template_name = 'students.html'
    context_object_name = 'students'

    def get_queryset(self):
        group = get_object_or_404(
            Groups,
            id=self.kwargs['group_id'],
            otm_id=self.kwargs['otm_id']
        )
        return Students.objects.filter(group=group).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        otm_id = self.kwargs['otm_id']
        group_id = self.kwargs['group_id']

        context['otm'] = get_object_or_404(Otm, id=otm_id)
        context['group'] = get_object_or_404(Groups, id=group_id)
        context['all_otm'] = Otm.objects.all()
        return context


def view_student(request, student_id):
    student = get_object_or_404(Students, id=student_id)
    return render(request, 'view_student.html', {'student': student})

class StudentDetailView(DetailView):
    model = Students
    template_name = 'view_student.html'
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'


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

class AddOtmView(CreateView):
    model = Otm
    form_class = OtmForm
    template_name = 'add_otm.html'
    success_url = reverse_lazy('home')


def add_group(request):
    if request.method=='POST':
        form=GroupForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=GroupForm()
    return render(request,'add_group.html',{'form':form})

class AddGroupView(CreateView):
    model = Groups
    form_class = GroupForm
    template_name = 'add_group.html'
    success_url = reverse_lazy('home')



def add_student(request):
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=StudentForm()
    return render(request,'add_student.html',{'form':form})

class AddStudentView(CreateView):
    model = Students
    form_class = StudentForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('home')


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

class UpdateOtmView(UpdateView):
    model = Otm
    form_class = OtmForm
    template_name = 'update_otm.html'
    pk_url_kwarg = 'otm_id'
    success_url = reverse_lazy('home')



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

class UpdateGroupView(UpdateView):
    model = Groups
    form_class = GroupForm
    template_name = 'update_group.html'
    pk_url_kwarg = 'group_id'
    success_url = reverse_lazy('home')



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

class UpdateStudentView(UpdateView):
    model = Students
    form_class = StudentForm
    template_name = 'update_student.html'
    pk_url_kwarg = 'student_id'
    success_url = reverse_lazy('home')


# #delete functions
def delete_otm(request,otm_id):
    otm=get_object_or_404(Otm,pk=otm_id)
    otm.delete()
    return redirect('home')

class DeleteOtmView(DeleteView):
    model = Otm
    pk_url_kwarg = 'otm_id'
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')


def delete_group(request,group_id):
    group=get_object_or_404(Groups,pk=group_id)
    group.delete()
    return redirect('home')

class DeleteGroupView(DeleteView):
    model = Groups
    pk_url_kwarg = 'group_id'
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')



def delete_student(request,student_id):
    student=get_object_or_404(Students,pk=student_id)
    student.delete()
    return redirect('home')

class DeleteStudentView(DeleteView):
    model = Students
    pk_url_kwarg = 'student_id'
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')
