from django.contrib import admin
from .models import System, SecurityEvent, AccessLog, Atack
from .models import Copyright

# Register your models here.
admin.site.register(System)
admin.site.register(SecurityEvent)
admin.site.register(Copyright)
admin.site.register(Atack)
