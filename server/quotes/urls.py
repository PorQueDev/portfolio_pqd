from django.urls import path
from .views import TodayQuoteView

urlpatterns = [
  path('quote-of-the-day/', TodayQuoteView.as_view(), name='today-quote'),
]