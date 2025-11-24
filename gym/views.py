from django.shortcuts import render


def home(request):
    """Vista principal del gimnasio."""
    return render(request, 'home.html')
