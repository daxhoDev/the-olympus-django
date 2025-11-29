from django.shortcuts import render, HttpResponse

# Create your views here.
def landing(request):
    context = {
        'plans': [
            {
                'name':'Standard',
                'price': '49',
                'plan_features': [
                    'Access to all gym facilities',
                    'Group fitness classes',
                    'Personalized workout plan'
                ],
                'isPremium': False
            },
            {
                'name':'Premium',
                'price': '79',
                'plan_features': [
                    'All Standard features',
                    'Unlimited personal training sessions',
                    'Exclusive wellness resources'
                ],
                'isPremium': True
            }
        ],
        'features': [
            {
                'title': 'State-of-the-Art Equipment',
                'description': 'Train with the latest machines and technology',
                'icon': '/dumbbell.svg'
            },
            {
                'title': 'Expert Trainers',
                'description': 'Certified professionals dedicated to your success',
                'icon': '/users.svg'
            },
            {
                'title': 'Open 24/7',
                'description': 'Workout anytime, day or night',
                'icon': '/clock.svg'
            },
        ]
    }
    return render(request, 'the_olympus/landing.html', context);

def register(request):
    return render(request, 'the_olympus/register.html', {})