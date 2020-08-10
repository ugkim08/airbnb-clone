from django.contrib import admin
from . import models

@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    
    """ Custom User Admin """

    # admin > user panel에 list_display 변수에 있는 항목들을 table에 추가해줌.
    # list_display = ("username", "email", "gender", "langauge", "currency", "superhost")
    # list_filter = ("langauge", "currency","superhost",)

    