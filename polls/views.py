import random,json
from itertools import chain
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.core import serializers
from django.db.models import Max
from .models import Question,Phpquestion,Userprof,ContactDetails,UserQuestions,Pythonquestion,Composition,Vocabulary,Document
from polls.forms import *
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def std(request):
    standard=request.POST.get('std')
    request.session['grade']=standard
    return render(request, 'test.html',{'stan':standard})


def test(request):
    return render(request, 'test.html')

def Compositionindex(request):
    if request.user.is_authenticated():
        cs=request.session['grade']
        comp=list(Composition.objects.filter(std=cs))
        random.shuffle(comp)
        form=DocumentForm()
        jlist=comp[:1]
        request.session['jlist'] = [j.q_id for j in jlist]
        return render(request,'single_input.html',{'latest_question_list': jlist,'form':form})
    else:
        return HttpResponseRedirect('/')

def Compositionresult(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'pic.html',
        {'documents': documents, 'form': form}
        
    )
def vocabindex(request):
    if request.user.is_authenticated():
        
        javapool = list(Vocabulary.objects.all())
        random.shuffle(javapool)
        jlist = javapool[:4]
        request.session['jlist'] = [j.q_id for j in jlist]
        return render(request,'index.html',{'latest_question_list': jlist})
    else:
        return HttpResponseRedirect('/')

def vocabresult(request):
    
    if request.user.is_authenticated():
        ch = []
        correct = 0
        idlist = request.session['jlist']
        jlist = []
        for i in idlist:
            jlist.append(Question.objects.get(pk=i))
        answers = []
        for j in jlist:
            answers.append(j.ans)

        for i in range(1,4):
            s = request.POST.get(str(i))
            if s:
                question, choice = s.split('-')
                ch.append(choice)
            else:
                ch.append(None)

        for i in range(0,3):
            if ch[i] == answers[i]:
                correct+=1
        if(correct>=7):
            lisst = zip(jlist,ch)

            up = Userprof.objects.create(username=request.user.username,subject='java',score=correct)
        else :
            request.session['std']-=1
            HttpResponseRedirect('test/vocabtest')
        return render(request,'result.html',{'qlist':lisst,'score':correct})
    else:
        return HttpResponseRedirect('/')



def compreindex(request):
    if request.user.is_authenticated():
        phppool = list(Phpquestion.objects.all())
        random.shuffle(phppool)
        phplist = phppool[:10]
        request.session['phplist'] = [p.q_id for p in phplist]
        return render(request,'index.html',{'latest_question_list': phplist})
    else:
        return HttpResponseRedirect('/')

def compreresult(request):
    if request.user.is_authenticated():
        ch = []
        correct = 0
        idlist = request.session['phplist']
        phplist = []
        for i in idlist:
            phplist.append(Phpquestion.objects.get(pk=i))
        answers = []
        for p in phplist:
            answers.append(p.ans)

        for i in range(1,11):
            s = request.POST.get(str(i))
            if s:
                question, choice = s.split('-')
                ch.append(choice)
            else:
                ch.append(None)
        
        for i in range(0,10):
            if ch[i] == answers[i]:
                correct+=1

        lisst = zip(phplist,ch)

        up = Userprof.objects.create(username=request.user.username,subject='php',score=correct)

        return render(request,'result.html',{'qlist':lisst,'score1':correct})
    else:
        return HttpResponseRedirect('/')

def mathindex(request):
    if request.user.is_authenticated():
        pypool = list(Pythonquestion.objects.all())
        random.shuffle(pypool)
        pylist = pypool[:10]
        request.session['pylist'] = [p.q_id for p in pylist]
        return render(request,'index.html',{'latest_question_list': pylist})
    else:
        return HttpResponseRedirect('/')

def mathresult(request):
    if request.user.is_authenticated():
        ch = []
        correct = 0
        idlist = request.session['pylist']
        pylist = []
        for i in idlist:
            pylist.append(Pythonquestion.objects.get(pk=i))
        answers = []
        for p in pylist:
            answers.append(p.ans)

        for i in range(1,11):
            s = request.POST.get(str(i))
            if s:
                question, choice = s.split('-')
                ch.append(choice)
            else:
                ch.append(None)

        for i in range(0,10):
            if ch[i] == answers[i]:
                correct+=1

        lisst = zip(pylist,ch)

        up = Userprof.objects.create(username=request.user.username,subject='python',score=correct)

        return render(request,'result.html',{'qlist':lisst,'score2':correct})
    else:
        return HttpResponseRedirect('/')


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            FormObj = ContactDetails(username=contact_name,email=contact_email,content=form_content)
            FormObj.save()
            # Email the profile with the 
            # contact information
            template = get_template('polls/contact_template.txt')
            context = {'contact_name': contact_name,'contact_email': contact_email,'form_content': form_content,}
            content = template.render({'context':context})
            email = EmailMessage(
                "New contact form submission",
                content,
                "LDD" +'',
                ['quizzy2016@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return HttpResponseRedirect('contact')
    return render(request, 'polls/contact.html', {'form': form_class,})

def submitq(request):
    form_class = QuestionForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            FormObj = UserQuestions(username=contact_name,email=contact_email,question=form_content)
            FormObj.save()

            # Email the profile with the 
            # contact information
            template = get_template('polls/question1.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render({'context':context})
            email = EmailMessage(
                "User has Entered",
                content,
                "" +'',
                [''],
                headers = {'': contact_email }
            )
            email.send()
            return HttpResponseRedirect('/submitq')

    return render(request, 'polls/question.html', {'form': form_class,})


def handler404(request):
    return render(request,'404.html')

def handler500(request):
    return render(request,'500.html')