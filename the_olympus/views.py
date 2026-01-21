from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from the_olympus.models import Plan, Profile
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone

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
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')
    return render(request, 'the_olympus/landing.html', context)

def user_dashboard(request):
    return render(request, 'the_olympus/user_dashboard.html')

class ProfilesListView(ListView):
    model = Profile
    template_name = 'the_olympus/admin_dashboard.html'
    context_object_name = 'profiles'
    
    def get_queryset(self):
        # Solo mostrar usuarios activos que no han sido eliminados
        return Profile.objects.filter(is_active=True, deleted_at__isnull=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Contar usuarios premium (excluyendo superusuarios y usuarios eliminados)
        context['premium_users_count'] = Profile.objects.filter(
            plan__is_premium=True,
            is_superuser=False,
            is_active=True,
            deleted_at__isnull=True
        ).count()
        context['standard_users_count'] = Profile.objects.filter(
            plan__is_premium=False,
            is_superuser=False,
            is_active=True,
            deleted_at__isnull=True
        ).count()

        return context

@login_required
@require_POST
def delete_user(request, user_id):
    """
    Realiza un soft delete del usuario estableciendo is_active=False y deleted_at
    """
    if not request.user.is_superuser:
        return redirect('admin_dashboard')
    
    user = get_object_or_404(Profile, id=user_id)
    
    # No permitir eliminar al propio usuario
    if user.id == request.user.id:
        return redirect('admin_dashboard')
    
    # Soft delete
    user.is_active = False
    user.deleted_at = timezone.now()
    user.save()
    
    return redirect('admin_dashboard')