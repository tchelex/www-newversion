from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Phone_call_back
from .forms import PhoneCallBackForm
from django.views.generic.edit import CreateView

class PhoneCallBackView(CreateView):
    template_name = 'landing/index.html'
    form_class = PhoneCallBackForm
    success_url = '/'


# def phone(request):
#     PhoneCallBackFormSet = modelformset_factory(Phone_call_back, form=PhoneCallBackForm)
#     if request.method == 'POST':
#         formset = PhoneCallBackFormSet(request.POST)
#         if formset.is_valid():
#             instance.save()
#             return redirect('home')
#     else:
#         formset = PhoneCallBackFormSet()
#     context =  {'formset': formset}
#     return render(request, 'landing/index.html', context)
