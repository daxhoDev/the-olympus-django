from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, CreateView
from the_olympus.models import Invitation, Plan, Profile, Payment
from the_olympus.forms import InvitationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

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
    payments = Payment.objects.filter(profile=request.user.id)
    context = {'payments': payments}
    return render(request, 'the_olympus/user_dashboard.html', context)

@login_required
def change_plan(request):
    """
    Permite al usuario cambiar su plan.
    GET: Muestra los planes disponibles
    POST: Actualiza el plan del usuario y crea un registro de pago
    """
    plans = Plan.objects.all()
    
    if request.method == 'POST':
        plan_id = request.POST.get('plan_id')
        if plan_id:
            new_plan = get_object_or_404(Plan, id=plan_id)
            
            # Actualizar el plan del usuario
            request.user.plan = new_plan
            request.user.save()
            
            # Crear registro de pago
            Payment.objects.create(
                profile=request.user,
                plan=new_plan,
                amount=new_plan.price
            )
            
            return redirect('dashboard')
    
    context = {
        'plans': plans,
        'current_plan': request.user.plan
    }
    return render(request, 'the_olympus/change_plan.html', context)

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

class CreateInvitation(CreateView):
    model = Invitation
    form_class = InvitationForm
    template_name = 'the_olympus/create_invitation.html'
    success_url = reverse_lazy('admin_dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Enviar correo de invitación
        invitation = self.object
        signup_url = self.request.build_absolute_uri(
            reverse('signup_with_token', kwargs={'token': invitation.token})
        )
        
        subject = 'You have been invited to The Olympus'
        message = f'''
Hello,

You have been invited to join The Olympus as a {invitation.get_role_display()}.

Please click the following link to complete your registration:
{signup_url}

Best regards,
The Olympus Team
        '''
        
        try:
            # Verificar que las credenciales de email estén configuradas
            if settings.EMAIL_HOST_USER and settings.EMAIL_HOST_PASSWORD:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [invitation.email],
                    fail_silently=True,  # No bloquear si falla el email
                )
            else:
                # Si no hay credenciales, solo imprimir en consola
                print(f'Email no enviado (credenciales no configuradas): {invitation.email}')
                print(f'URL de invitación: {signup_url}')
        except Exception as e:
            # Log del error pero no crashear la aplicación
            print(f'Error al enviar email: {e}')
            print(f'URL de invitación para {invitation.email}: {signup_url}')
        
        return response 