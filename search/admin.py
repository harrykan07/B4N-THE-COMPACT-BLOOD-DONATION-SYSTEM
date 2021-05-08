from django.contrib import admin
from .models import SearchLogo
from .models import RequestedRecord
from .models import Points


admin.site.register(SearchLogo)
admin.site.register(RequestedRecord)
admin.site.register(Points)


