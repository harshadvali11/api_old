from django.contrib import admin
from myapp.models import UserProfile,SampleModel
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(SampleModel)