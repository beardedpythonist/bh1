from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'user_id')
    search_fields = ('last_name', )

@admin.register(GroupUsers)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'group_id',)
    search_fields = ('user_id',)

@admin.register(Group)
class UserAdmin(admin.ModelAdmin):
    list_display = ('number', )
    search_fields = ('number', )

@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ('number', )
    search_fields = ('number', )

@admin.register(Training_Format)
class  Training_Format(admin.ModelAdmin):
    list_display = ('is_online',)
    search_fields = ('is_online',)

@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('name','price')
    search_fields = ('name','price')





