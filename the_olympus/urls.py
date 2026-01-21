from django.urls import path
from the_olympus.views import CreateInvitation, landing, user_dashboard, ProfilesListView, delete_user
urlpatterns = [

    path('', landing, name='landing'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('admin-dashboard', ProfilesListView.as_view(), name='admin_dashboard'),
    path('user/delete/<int:user_id>/', delete_user, name='delete_user'),
    path('invitation/create/', CreateInvitation.as_view(), name='create_invitation'),
    ]