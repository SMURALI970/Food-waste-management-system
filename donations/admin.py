from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['donor_name', 'food_item', 'quantity', 'location', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['donor_name', 'food_item', 'location']