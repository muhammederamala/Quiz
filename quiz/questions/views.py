from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from .models import quiz_model
from django.views.decorators.csrf import csrf_protect

from .forms import quiz_form
# Create your views here.

def home(request):
	print(request.headers)
	return render(request, "questions/home.html",{})

def quiz_list_view(request):
	print(request.headers)
	quiz = quiz_model.objects.all()
	return render(request, "questions/quiz_list.html",{'quiz' : quiz})


@csrf_protect
def add_quiz_view(request):
	if request.method == 'POST':
		form = quiz_form(request.POST)
		if form.is_valid():
			question = form.cleaned_data[ 'question']
			option1 = form.cleaned_data['option1']
			option2 = form.cleaned_data['option2']
			option3 = form.cleaned_data['option3']
			option4 = form.cleaned_data['option4']
			right_answer_index = form.cleaned_data['right_answer_index']
			start_date = form.cleaned_data['start_date']
			end_date = form.cleaned_data['end_date']
			
			new_quiz_model = form.save(commit=False)
			new_quiz_model.save()
			quiz = quiz_model.objects
			new_quiz_model.update_status()
			return redirect('quiz_list_view')
		else:
			form = quiz_form(request.POST)
			print(form.errors)
	else:
		form = quiz_form()
	return render(request, 'questions/home.html', {'form': form})

def delete_quiz_view(request, new_quiz_id):
	try:
		quiz_to_delete = quiz_model.objects.get(pk=new_quiz_id,)
	except quiz_model.DoesNotExist:
		raise Http404("Class does not exist or does not belong to user.")
	quiz_to_delete.delete()
	return redirect('quiz_list_view')