from django.urls import path
from .views import upgrade_me, BaseRegisterView

urlpatterns = [
    path('upgrade/', upgrade_me, name='upgrade'),
]
