from clg.models import *
from django.db import models

class Payments(models.Model):
    college_fee = models.IntegerField(null=False, default=0)
    jntugv_fee = models.IntegerField(null=False, default=0)
    exam_fee = models.IntegerField(null=False, default=0)
    dou = models.DateField(auto_now=True)


    def __str__(self):
        return f"{self.college_fee} {self.jntugv_fee} {self.exam_fee} {self.dou}"


class SpecialFee(models.Model):
    spe_fee = models.IntegerField(null=True)
    spe_for = models.CharField(max_length=1000, default="")
    doc = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.spe_fee} {self.spe_for} {self.doc}"
