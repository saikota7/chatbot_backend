from django.urls import path
from .views import ChatbotView

urlpatterns = [
    path('messages/', ChatbotView.as_view(), name='chatbot'),
]

