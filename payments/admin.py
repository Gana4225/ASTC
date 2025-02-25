from django.contrib import admin
from .models import *


class Payments1(admin.ModelAdmin):
    list_display = ["jntugv_fee", "college_fee", "exam_fee", "dou"]


class Spe(admin.ModelAdmin):
    list_display = ["spe_fee", "spe_for", "doc"]

class Recp(admin.ModelAdmin):
    list_display = ["roll_number", "name", "pay_id", "department", "regulation", "dop"]


admin.site.register(Payments, Payments1)
admin.site.register(SpecialFee, Spe)


