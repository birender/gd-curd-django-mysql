from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentModel
from .forms import StudentForm
from django.contrib import messages

def studentList(request):
	qs = StudentModel.objects.all()
	context = {
		"object": qs
	}
	return render(request, 'student/list.html', context)

def studentCreate(request):
	form = StudentForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		messages.success(request,"successfully Created!!")
		return redirect("list")
	else:
		messages.error(request,form.errors)
	return render(request, 'student/create.html', context)

def studentUpdate(request,id):
	qs = get_object_or_404(StudentModel, id=id)
	form = StudentForm(request.POST or None, instance=qs)
	context = {
		"form": form
	}
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		return redirect("list")
	return render(request, 'student/create.html', context)

def studentDelete(request,id):
	qs = get_object_or_404(StudentModel, id=id)	
	if qs:
		qs.delete()
	return redirect("list")
