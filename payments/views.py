import razorpay
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Payments, SpecialFee
from clg.models import *


def payments(amount):
    client = razorpay.Client(auth=("rzp_test_F4KAIVewl3a2UP", "hPfWC0HrQlkaxHtaWtSUllrF"))
    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return payment


def home(request):
    return render(request, 'payments/pay.html')

@csrf_exempt
def cnfm(request):
    if request.method == "POST":
        fee_type = int(request.POST.get('type'))
        user = request.session.get("user_id")
        data = Payments.objects.get(id=3)
        rdata = Re.objects.get(user_name=user)
        sdata = Student.objects.get(roll_number=rdata.roll_number.roll_number)
        if fee_type == 1:
            p = amount = data.jntugv_fee * 100
            p = p//100
            purpose = "JNTUGV FEE"
            payments(amount)
            return render(request, "payments/pdetails.html",
                          {"payment":payments,"sdata":sdata, "pur":purpose, "p":p, "amount":amount})

        if fee_type == 2:
            p = amount = data.college_fee * 100
            p = p // 100
            purpose = "COLLEGE FEE"
            payments(amount)
            return render(request, "payments/pdetails.html",
                          {"payment": payments, "sdata": sdata, "pur": purpose, "p": p, "amount": amount})


        if fee_type == 3:
            p = amount = data.exam_fee * 100
            p = p // 100
            purpose = "EXAM FEE"
            payments(amount)
            return render(request, "payments/pdetails.html",
                          {"payment": payments, "sdata": sdata, "pur": purpose, "p": p, "amount": amount})

        spedata = SpecialFee.objects.get(id=2)


        if fee_type == 4:
            p = amount = spedata.spe_fee * 100
            p = p // 100
            purpose = spedata.spe_for
            payments(amount)
            return render(request, "payments/pdetails.html",
                          {"payment": payments, "sdata": sdata, "pur": purpose, "p": p, "amount": amount})

        return HttpResponse("Invalid request")

    return HttpResponse("Invalid request please try again")

@csrf_exempt
def pay(request):
   if request.method == "POST":
       pid = request.POST.get('payment_id')
       client = razorpay.Client(auth=("rzp_test_F4KAIVewl3a2UP", "hPfWC0HrQlkaxHtaWtSUllrF"))
       payment_status = client.payment.fetch(pid)
       oid = payment_status['description']
       ccc = payment_status["acquirer_data"]
       rrn = payment_status.get("acquirer_data", {}).get("rrn", "RRN Not Available")
       context = {"pid":pid, "oid":oid, "utr":rrn, "amount":payment_status['amount']//100,}
       if payment_status["status"] == "captured":

           return render(request, "payments/status.html", context)

       else:

           capture = client.payment.capture(pid, payment_status["amount"])

           return render(request, "payments/status.html", context)





"""

{'id': 'pay_Q0FTYfOONscc3h', 'entity': 'payment', 'amount': 80000, 'currency': 'INR', 'status':
 'captured', 'order_id': None, 'invoice_id': None, 'international': False, 'method': 'upi', 'am
ount_refunded': 0, 'refund_status': None, 'captured': True, 'description': 'EXAM FEE', 'card_id
': None, 'bank': None, 'wallet': None, 'vpa': 'sdf@ybl', 'email': 'ch.gana@gmail.com', 'contact
': '+917898282609', 'notes': [], 'fee': 1888, 'tax': 288, 'error_code': None, 'error_descriptio
n': None, 'error_source': None, 'error_step': None, 'error_reason': None, 'acquirer_data': {'rr
n': '812258928960', 'upi_transaction_id': '93824430602AC90E232E6D06F19C4EEA'}, 'created_at': 1740553153, 'upi': {'vpa': 'sdf@ybl'}}

"""