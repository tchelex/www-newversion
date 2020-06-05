from django.contrib import admin
from .models import Phone_call_back

class Phone_call_back_Admin(admin.ModelAdmin):
    model = Phone_call_back
    list_display = ('first_name', 'last_name', 'phone')

admin.site.register(Phone_call_back, Phone_call_back_Admin)
