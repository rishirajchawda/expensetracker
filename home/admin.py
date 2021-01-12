from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import * 


class UserAdd(admin.StackedInline):
	model=Profile
class UserPanel(UserAdmin):	
	inlines=[UserAdd]



admin.site.unregister(User)
admin.site.register(User,UserPanel)
# Register your models here.

admin.site.register(Profile)
admin.site.register(Expense)
