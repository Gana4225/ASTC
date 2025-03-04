from django.views.decorators.csrf import csrf_exempt
from .utils import *
from payments.models import *
from clg.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps
from django.forms import modelform_factory
from django.http import JsonResponse


def realhome(request):
    user = request.session.get("user_id")
    return render(request, "clg/master.html", {"user": user})


def home(request):
    if not check_user_logged_in(request):
        return render(request, 'clg/login.html')
    return redirect('dashboard')


@csrf_exempt
def log(request):
    if request.method == "POST":
        user = request.POST['username']
        password = request.POST['password']

        try:

            data = Re.objects.get(user_name=user)
            if check_password(password, data.password):

                request.session['user_id'] = data.user_name
                request.session['last_activity'] = datetime.now().timestamp()
                return redirect('dashboard')

            else:

                return HttpResponse('invalid password')

        except Exception:

            a = 1
            return render(request, "clg/error.html",
                          context={'user': user, 'a': a})

    if not check_user_logged_in(request):

        return redirect('home')
    else:
        return redirect('dashboard')


# view for logout
def clogout(request):
    try:

        del request.session['user_id']
        del request.session['last_activity']

    except KeyError:

        pass

    return redirect('realhome')


# view for user registration

def reg(request):
    if request.method == 'GET':
        return handle_get_request(request)

    if request.method == 'POST':

        if 'otp' in request.POST:

            return handle_otp_verification(request)

        else:

            return handle_registration(request)

    return HttpResponse("<h1>Invalid request method</h1>")


def dashboard(request):
    if not check_user_logged_in(request):
        return redirect('login')

    return render(request, 'clg/dashboard.html')


def about(request):
    return render(request, 'clg/about.html')


def pay(request):
    if not check_user_logged_in(request):
        return redirect('realhome')

    return redirect('second/')


def otp(request):
    return render(request, 'clg/otp.html')


def stdprofile(request):
    if not check_user_logged_in(request):
        return redirect('realhome')

    try:
        a = request.session.get('user_id')
        b = Re.objects.get(user_name=a)
        c = Student.objects.get(roll_number=b.roll_number.roll_number)

        if not c.image:
            c.image = None  # You can set a default image URL if needed
        return render(request, 'clg/stdprofile.html', {'student': c, 'a': a})
    except Exception as e:
        print(e)
        return HttpResponse("image error")


def update_profile(request):
    if not check_user_logged_in(request):
        return redirect('realhome')

    return updatepf(request)


def dd(request):
    return render(request, 'clg/login.html')


def contact(request):
    return render(request, "clg/contact.html")


def admission(request):
    return render(request, "clg/admissionprocess.html")


def departments(request):
    return render(request, "clg/departments.html")


def placements(request):
    data = Placements.objects.all()
    return render(request, "clg/placements.html", {"data":data})


def activities(request):
    return render(request, "clg/activities.html")


def research(request):
    return render(request,"clg/researches.html")


def amenities(request):
    return render(request, "clg/amenities.html")