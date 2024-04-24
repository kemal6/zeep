from django.contrib import admin
from .models import CustomUser,PatternStamp,Monture

admin.site.register(CustomUser)
admin.site.register(PatternStamp)
admin.site.register(Monture)

# Register your models here.
