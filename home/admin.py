from django.contrib import admin
from .models import Advisor, Customer, Booking

# Register your models here.
admin.site.register(Advisor),
admin.site.register(Customer),
admin.site.register(Booking),

