from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import AppealForm
from .models import *


def home(request):
    applicants_panel_info = Applicants_panel.objects.first()
    socials = Social.objects.all()
    appealForm = AppealForm()
    answers = False

    if request.POST.get('answer_code'):
        code = request.POST.get('answer_code')
        appeal = Appeal.objects.get(code=code)
        answers = Answer.objects.get(appeal=appeal)

        # messages.success(request, f'{answers}, {answers.text}')
        return redirect('home')
        
        
    elif request.POST:

        appealForm = AppealForm(request.POST, request.FILES)
        if appealForm.is_valid():
            obj = appealForm.save(commit=False)
            obj.save()

            messages.success(request, f"Bu sizning javobni korish uchun parolingiz, Ishonchli joyga saqlab qoying!!!{obj.code}")
            return redirect('home')
        
    context = {
        'appealForm': appealForm,
        'applicants_panel_info': applicants_panel_info,
        'socials': socials,
    }
    
    if answers:
        context['answers'] = answers

    return render(request, 'index.html', context)