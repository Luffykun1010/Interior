from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(company)
admin.site.register(sub_works)
admin.site.register(user)
admin.site.register(workers)
admin.site.register(works)
admin.site.register(contract_details)