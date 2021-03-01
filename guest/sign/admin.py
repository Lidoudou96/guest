from django.contrib import admin
from sign.models import Event,Guest
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','limit','address','start_time']
    search_fields = ['name']
    list_filter = ['status']
class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','event','create_time']
    search_fields = ['realname','phone']
    list_filter = ['sign']
admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)