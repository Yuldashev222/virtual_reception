from django.shortcuts import redirect, render

from .forms import AppealForm
from .models import *


def home(request):
    applicants_panel_info = Applicants_panel.objects.first()
    appealForm = AppealForm()

    if request.POST:
        appealForm = AppealForm(request.POST or None, request.FILES or None)
        print(request.POST)
        if appealForm.is_valid():
            print('/////////////////////3')
            appeal = appealForm.save(commit=False)
            appeal.save()

            return redirect('home')

    context = {
        'appealForm': appealForm,
        'applicants_panel_info': applicants_panel_info,
    }

    return render(request, 'index.html', context)