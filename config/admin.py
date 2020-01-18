from django.contrib import admin
from .models import SideBar, Link

from django_blog.custom_site import custom_site
from django_blog.base_admin import BaseOwnerAdmin

# Register your models here.


@admin.register(SideBar,site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')




@admin.register(Link,site=custom_site)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')

