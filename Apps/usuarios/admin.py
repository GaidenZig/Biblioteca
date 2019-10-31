from django.contrib import admin,auth
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm
from .models import MyUser

# Register your models here.
class UserAdmmin(BaseUserAdmin):
    add_form = UserCreationForm
    list_display = ('username', 'email', 'is_superuser','activo')
    list_filter=('is_superuser',)

    fieldsets=(
        (None, {'fields':('username','email', 'password','activo','descripcion','img_perfil')}),
        ('Permissions', {'fields':('is_superuser','is_staff')})
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'email' )
    filter_horizontal= ()

admin.site.register(MyUser, UserAdmmin)
admin.site.unregister(Group)

