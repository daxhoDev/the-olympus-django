from django.shortcuts import render
from django.views.generic import ListView
from the_olympus.models import Plan, Profile

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

class ProfilesListView(ListView):
    model = Profile
    template_name = 'the_olympus/admin_dashboard.html'
    context_object_name = 'profiles'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Contar usuarios premium (excluyendo superusuarios y usuarios eliminados)
        context['premium_users_count'] = Profile.objects.filter(
            plan__is_premium=True,
            is_superuser=False,
        ).count()
        context['standard_users_count'] = Profile.objects.filter(
            plan__is_premium=False,
            is_superuser=False,
        ).count()

        return context