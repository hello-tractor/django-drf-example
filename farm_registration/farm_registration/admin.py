from django.contrib import admin
from myapp.models import Farmer, Farm
from django.contrib.auth.models import User, Group, Permission
site = admin.AdminSite()


site.register(User)
site.register(Group)
site.register(Permission)

site.register(Farmer)

class FarmAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'area']
    list_filter = ['owner', 'area']

site.register(Farm, FarmAdmin)