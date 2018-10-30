from django.contrib import admin

from .models import Property_Images, Property_Facing, Property, Property_Sector, Property_Category, Province, City, Country
from .models import  User, UserRole, RolePermission, RoleCode, Password, PermissionType
# Register your models here.





admin.site.register(Property_Images)
admin.site.register(Property)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)


admin.site.register(User)
admin.site.register(UserRole)

admin.site.register(RolePermission)
admin.site.register(RoleCode)
admin.site.register(Password)
admin.site.register(PermissionType)
