from django.contrib import admin
from .models import Lead
# Register your models here.


class LeadAdmin(admin.ModelAdmin):
	list_display = ['firstname','lastname','email','timestamp']
	class Meta:
		model = Lead

admin.site.register(Lead,LeadAdmin)