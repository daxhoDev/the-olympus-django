from django.contrib import admin

from the_olympus.models import Invitation, Payment, Plan, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Plan)
admin.site.register(Payment)
admin.site.register(Invitation)
admin.site.site_header = "The Olympus Admin"
admin.site.site_title = "The Olympus Admin Portal"