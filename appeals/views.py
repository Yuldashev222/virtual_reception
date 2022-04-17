from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import AppealForm
from .models import *


def home(request):
    all_appeals_cnt = Appeal.objects.all().count()
    process_appeals_cnt = Appeal.objects.filter(appeal_status='process').count()
    rejected_appeals_cnt = Appeal.objects.filter(appeal_status='rejected').count()
    completed_appeals_cnt = Appeal.objects.filter(appeal_status='completed').count()
    new_appeals_cnt = Appeal.objects.filter(appeal_status='new').count()
    
    
    applicants_panel_info = Applicants_panel.objects.first()
    socials = Social.objects.all()
    appealForm = AppealForm()
    answers = False
    
    context = {
        'appealForm': appealForm,
        'applicants_panel_info': applicants_panel_info,
        'socials': socials,

        
        'all_appeals_cnt': all_appeals_cnt,
        'process_appeals_cnt': process_appeals_cnt,
        'rejected_appeals_cnt': rejected_appeals_cnt,
        'completed_appeals_cnt': completed_appeals_cnt,
        'new_appeals_cnt': new_appeals_cnt,
    }

    if request.POST:
        if request.POST.get('answer_code'):

            code = request.POST.get('answer_code')
            appeal = Appeal.objects.get(code=code)
            answers = Answer.objects.get(appeal=appeal)

            # messages.success(request, f'{answers}, {answers.text}')
            return redirect('home')
        
        
        else:
            appealForm = AppealForm(request.POST, request.FILES)

            if appealForm.is_valid():
                obj = appealForm.save(commit=False)
                obj.save()

                # messages.success(request, f"Bu sizning javobni korish uchun parolingiz, Ishonchli joyga saqlab qoying!!!{obj.code}")
                return redirect('home')
        
    
    if answers:
        context['answers'] = answers

    return render(request, 'index.html', context)