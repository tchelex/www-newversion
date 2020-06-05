from django import forms

from .models import Phone_call_back


class PhoneCallBackForm(forms.ModelForm):
    class Meta:
        model = Phone_call_back
        # fields = ['first_name',
        #           'last_name',
        #           'phone']
        fields = '__all__'