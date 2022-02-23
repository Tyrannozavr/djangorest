app_name = 'support'
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = [
    path('', root, name='root'),
    path('tickets/', TicketList.as_view(), name='tickets-list'),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name='tickets-detail'),
    path('messages/', MessageList.as_view(), name='message-list'),
    path('messages/<int:pk>/', MessageDetail.as_view(), name='message-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)