from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.decorators import register
# Register your models here.
from .models import Account
@register(Account)
class AccountAdmin(UserAdmin):
    list_display=['email','first_name','last_name']
    list_display_links=['email','first_name','last_name']

    filter_horizontal=()
    list_filter=()