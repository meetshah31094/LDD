from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from forms import RegistrationForm

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            #send_mail(subject,message,from_email,to_list,fail_silently=True)
            subject = 'Hello from QUIZZY'
            message = 'Hi there, ' + request.POST['username'] +'\nThanks for registering with us. Please visit our site to take a test now (quizzy.pythonanywhere.com)'
            from_email = settings.EMAIL_HOST_USER
            to_list = [request.POST['email']]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            return render(request,'login/success.html',{'user':user})
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('login/register.html',variables)

def register_success(request):
    return render(request,'login/success.html') 

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response('home.html',{ 'user': request.user })

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if(username == "master"):
                return render(request,'master_base.html',{'user':user})

            if user.is_active:
                login(request, user)
                return render(request,'base.html',{'user':user})
            else:
                return HttpResponse("This user account is disabled.")
        else:
            msg = 'Invalid credentials. Try again.'
            return render(request,'login/login.html',{'msg':msg})
    else:
        return render(request,'login/login.html')
