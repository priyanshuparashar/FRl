from django.contrib import admin
from .models import *


admin.site.register(UserProfile)
admin.site.register(PropertyType)
admin.site.register(Property)
admin.site.register(Transaction)
# Register your models here.
