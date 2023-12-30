from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')

    def id(self, obj):
        return obj.customer.id

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name


class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customer'


class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInline,)


admin.site.register(Customer, CustomerAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
