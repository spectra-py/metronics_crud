from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUsers
from blog.models import Post
from dashboard.models import profile

# Register your models here.


# Register your models here.





class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUsers
    list_display = ('email', 'is_staff', 'is_active','username','first_name','middle_name')
    list_filter = ('email', 'is_staff', 'is_active','username','first_name','middle_name')
    fieldsets = (
        (None, {'fields': ('email', 'password','username','first_name','middle_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','first_name','middle_name', 'password1', 'password2', 'is_staff', 'is_active',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUsers, CustomUserAdmin)
admin.site.register(Post)
admin.site.register(profile)