from django.urls import path
from django.views.generic.base import TemplateView
from .views import PhoneCallBackView
# from .views import phone

urlpatterns = [
    path('',
         PhoneCallBackView.as_view(),
         name='home'),
    # path('',
    #      phone,
    #      name='home'),
]
