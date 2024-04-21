from django.contrib import admin
from .models import CustomUser,PatternStamp

admin.site.register(CustomUser)
admin.site.register(PatternStamp)

# Register your models here.
