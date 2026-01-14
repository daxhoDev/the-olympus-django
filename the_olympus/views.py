from django.shortcuts import render, HttpResponse

from the_olympus.models import Plan

# Create your views here.
def landing(request):
    context = {
        'plans': Plan.objects.all(),
        'features': [
            {
                'title': 'State-of-the-Art Equipment',
                'description': 'Train with the latest machines and technology',
                'icon': 'dumbbell.svg'
            },
            {
                'title': 'Expert Trainers',
                'description': 'Certified professionals dedicated to your success',
                'icon': 'users.svg'
            },
            {
                'title': 'Open 24/7',
                'description': 'Workout anytime, day or night',
                'icon': 'clock.svg'
            },
        ]
    }
    return render(request, 'the_olympus/landing.html', context)

def user_dashboard(request):
    return render(request, 'the_olympus/user_dashboard.html')