from django.urls import path
from the_olympus.views import landing, user_dashboard

urlpatterns = [

    path('', landing, name='landing'),
    path('dashboard/', user_dashboard, name='dashboard'),]