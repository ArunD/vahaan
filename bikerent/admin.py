from django.contrib import admin
from bikerent.models import BikeDetail,BikeType


#class BikeAdmin(admin.ModelAdmin):



admin.site.register(BikeType)
admin.site.register(BikeDetail)


# Register your models here.
