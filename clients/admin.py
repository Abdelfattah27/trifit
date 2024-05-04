from django.contrib import admin
from django.utils import timezone
from datetime import timedelta
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'age', 'gender', 'plan', 'join_date', 'expire_date', 'days_until_expire')
    ordering = ('expire_date',) 
    search_fields = ["name"]
    list_display_links = ('name', 'contact', 'age', 'gender', 'plan', 'join_date', 'expire_date', 'days_until_expire')
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save_and_continue'] = False
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def days_until_expire(self, obj):
        expire_date = obj.expire_date
        today = timezone.now().date()
        days_left = (expire_date - today).days
        return days_left if days_left >= 0 else 0
    days_until_expire.admin_order_field = 'expire_date' 

admin.site.register(Member, MemberAdmin)
