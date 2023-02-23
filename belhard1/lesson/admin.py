from django.contrib import admin
from django.contrib.admin.options import StackedInline, TabularInline
from .models import *



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('last_name',)

@admin.register(GroupUsers)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'group_id',)
    search_fields = ('user_id',)




@admin.register(Group)
class UserAdmin(admin.ModelAdmin):
    list_display = ('number',)
    search_fields = ('number',)


@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ('number',)
    search_fields = ('number',)


@admin.register(Training_Format)
class Training_Format(admin.ModelAdmin):
    list_display = ('is_online',)
    search_fields = ('is_online',)


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')


@admin.register(Payment_info)
class PaymentInfo(admin.ModelAdmin):
    list_display = ('sec_paid_date', 'sec_paid_amount')
    search_fields = ('sec_paid_date', 'sec_paid_amount')


@admin.register(Role)
class RoleInfo(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(RolePermission)
class RolePermission(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Permission)
class Permis(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ('day',)
    search_fields = ('day',)


@admin.register(LessonMaterial)
class LessonMaterial(admin.ModelAdmin):
    list_display = ('url', 'file',)
    search_fields = ('url', 'file',)


@admin.register(Feedback)
class Feedback(admin.ModelAdmin):
    list_display = ('text',)
    search_fields = ('text',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
