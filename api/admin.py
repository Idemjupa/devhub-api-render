from django.contrib import admin

# Register your models here.

from .models import (
    Category,Candidate,
    Type, Company, Location
)

admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Company)
admin.site.register(Candidate)
admin.site.register(Location)
