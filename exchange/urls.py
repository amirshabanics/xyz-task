from django.urls import path
from exchange.views import IndexView

urlpatterns = [
    path('index/', IndexView.as_view()),
]
