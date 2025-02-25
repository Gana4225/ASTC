import razorpay
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Payments, SpecialFee
from clg.models import *



def home(request):
    return render(request, 'payments/pay.html')

@csrf_exempt
def cnfm(request):
    if request.method == "POST":
        fee_type = int(request.POST.get('type'))
        user = request.session.get("user_id")
        data = Payments.objects.get(id=1)
        rdata = Re.objects.get(user_name=user)
        sdata = Student.objects.get(roll_number=rdata.roll_number.roll_number)
        if fee_type == 1:
            p = amount = 1 * 100
            p = p//100
            purpose = "JNTUGV FEE"
            client = razorpay.Client(auth=("rzp_live_vFZrNfs1Qu9cx4", "B8zpbYSMCee3yDJarwOuyqH8"))
            payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
            return render(request, "payments/pdetails.html",
                          {"payment":payment,"sdata":sdata, "pur":purpose, "p":p})

        if fee_type == 2:
            p = amount = data.college_fee * 100
            p = p // 100
            purpose = "COLLEGE FEE"
            client = razorpay.Client(auth=("rzp_live_vFZrNfs1Qu9cx4", "B8zpbYSMCee3yDJarwOuyqH8"))
            payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
            return render(request, "payments/pdetails.html",
                          {"payment":payment,"sdata":sdata, "pur":purpose, "p":p})

        if fee_type == 3:
            p = amount = data.exam_fee * 100
            p = p // 100
            purpose = "EXAM FEE"
            client = razorpay.Client(auth=("rzp_live_vFZrNfs1Qu9cx4", "B8zpbYSMCee3yDJarwOuyqH8"))
            payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
            return render(request, "payments/pdetails.html",
                          {"payment":payment,"sdata":sdata, "pur":purpose, "p":p})

        spedata = SpecialFee.objects.get(id=1)


        if fee_type == 4:
            p = amount = spedata.spe_fee * 100
            p = p // 100
            purpose = spedata.spe_for
            client = razorpay.Client(auth=("rzp_live_vFZrNfs1Qu9cx4", "B8zpbYSMCee3yDJarwOuyqH8"))
            payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
            return render(request, "payments/pdetails.html",
                          {"payment":payment,"sdata":sdata, "pur":purpose, "p":p})

        return HttpResponse("hello")

    return HttpResponse("gvhjbkn")

@csrf_exempt
def pay(request):
   if request.method == "POST":
       pid = request.POST.get('payment_id')
       oid = request.POST.get('order_id')
       utr = request.POST.get('utr')
       client = razorpay.Client(auth=("rzp_live_vFZrNfs1Qu9cx4", "B8zpbYSMCee3yDJarwOuyqH8"))
       payment_status = client.payment.fetch(pid)
       ccc = payment_status["acquirer_data"]
       print(ccc['rrn'])
       rrn = payment_status.get("acquirer_data", {}).get("rrn", "RRN Not Available")
       print(rrn)
       print(payment_status)
       context = {"pid":pid,
                  "oid":oid,
                  "utr":utr}
       return render(request, "payments/status.html", context)
