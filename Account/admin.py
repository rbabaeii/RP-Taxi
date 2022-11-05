from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets[2][1]['fields'] = (
                                        "is_driver",
                                        "is_active",
                                        "is_staff",
                                        "is_superuser",
                                        "phone",
                                        "Address",
                                        "Age",
                                        "gender",
                                        "groups",
                                        "user_permissions",

)

admin.site.register(User, UserAdmin)