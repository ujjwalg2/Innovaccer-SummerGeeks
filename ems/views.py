from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from datetime import datetime
from django.core.mail import send_mail
from django_twilio.client import twilio_client
# Create your views here.

def index(request):
    form = UserForm()
    hosts = Host.objects.filter(offline=False)
    context = {
        'form': form,
        'hosts': hosts,
    }
    return render(request, 'index.html', context)

def mail(userType, visitor, host):
    to_email = []
    if userType == 'Host':
        mail_subject = 'A visitor has arrived'
        to = str(host.user.email)
        message = "Hi "+host.user.firstname+" "+host.user.lastname+",\nVisitor Details:\nName - "+visitor.user.firstname+" "+visitor.user.lastname+"\nEmail - "+visitor.user.email+"\nPhone - "+visitor.user.contact+"\nCheckIn Time - "+str(visitor.checkIn)
    elif userType == 'Visitor':
        mail_subject = 'Thanks for visiting us!'
        to = str(visitor.user.email)
        message = "Hi "+visitor.user.firstname+" "+visitor.user.lastname+",\nName - "+visitor.user.firstname+" "+visitor.user.lastname+"\nPhone - "+visitor.user.contact+"\nEmail Address - "+visitor.user.email+"\nCheckIn Time - "+str(visitor.checkIn)+"\nCheckOut Time - "+str(visitor.checkOut)+"\nHost Name - "+host.user.firstname+" "+host.user.lastname
    to_email.append(to)
    from_email = 'shikari9000@gmail.com'
    send_mail(
        mail_subject,
        message,
        from_email,
        to_email,
    )

def sms():
    message = twilio_client.messages.create(
                to='+918318799361', 
                from_='+19513970207', 
                body='Hey! OTP for your MINU account is'
            )

def checkIn(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            hostEmail = request.POST['hostEmail']
            hostUser = User.objects.get(email=hostEmail)
            host = Host.objects.get(user=hostUser)
            host.offline = True
            host.save()

            checkIn = datetime.now()
            visitor = Visitor.objects.create(user=user, host=host, checkIn=checkIn)
            visitor.save()
            mail('Host', visitor, host)
            sms()
        return redirect('http://localhost:8000/')
    else:
        return render(request, '/', {})

def checkOut(request):
    if request.method == "POST":
        visitorEmail = request.POST['email']
        visitorContact = request.POST['contact']

        try:
            visitorUser = User.objects.get(email=visitorEmail, contact=visitorContact)
        except User.DoesNotExist:
            error_msg = "User with the given details does not exists"
            form = UserForm()
            hosts = Host.objects.filter(offline=False)
            context = {
                'form': form,
                'hosts': hosts,
                'error': error_msg,
            }
            return render(request, 'index.html', context)

        try:
            visitor = Visitor.objects.get(user=visitorUser)
        except Visitor.DoesNotExist:
            error_msg = "Visitor with the given details does not exists"
            form = UserForm()
            hosts = Host.objects.filter(offline=False)
            context = {
                'form': form,
                'hosts': hosts,
                'error': error_msg,
            }
            return render(request, 'index.html', context)

        if visitor.checkOut:
            error_msg = "Visitor is already checked out"
            form = UserForm()
            hosts = Host.objects.filter(offline=False)
            context = {
                'form': form,
                'hosts': hosts,
                'error': error_msg,
            }
            return render(request, 'index.html', context)

        if visitor.checkOut is None:
            visitor.checkOut = datetime.now()
            host = visitor.host
            host.offline = False
            host.save()
            visitor.save()
            mail('Visitor', visitor, host)
            visitorUser.delete()
            return redirect('http://localhost:8000/')
        return redirect('http://localhost:8000/')
    else:
        return render(request, '/', {})

def hostRegistration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            host = Host.objects.create(user=user)
            host.save()
        return redirect('http://localhost:8000/')
    else:
        return render(request, '/', {})