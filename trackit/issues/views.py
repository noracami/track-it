from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Label
import hashlib

# Create your views here.
def home(request):
    issue = Ticket.objects.filter().order_by('-id')
    readit = []
    for i in issue:
        issue_get = {}
        issue_get['id'] = i.id
        issue_get['title'] = i.ticket_title
        issue_get['status'] = i.status
        issue_get['time'] = i.time
        issue_get['label'] = i.label_set.all()
        readit.append(issue_get)
        #pass
    return render(request, 'home.html', {"readit": readit, "request": request})

def issues(request, ticket_id):
    issue = get_object_or_404(Ticket, id=ticket_id)
    issue_get = {}
    issue_get['id'] = issue.id
    issue_get['title'] = issue.ticket_title
    issue_get['status'] = issue.status
    issue_get['time'] = issue.time
    issue_get['label'] = issue.label_set.all()
    return render(request, 'issues.html', {"issue_get": issue_get, "request": request})

def newissues(request):
    if "login" in request.session:
        name = request.session['login']
    else:
        name = "default"
    return render(request, 'newissues.html', {"issue_get": name, "request": request})

def loginhere(request):

    return render(request, 'loginhere.html', {"issue_get": "", "request": request})

def login(request):
    #TODO rewrite please
    if request.method == 'POST':
        if request.POST['login_password']:
            plain = request.POST['login_password']
            if hashlib.sha224(plain.encode()).hexdigest() == '71454996db126e238e278a202a7dbc49dda187ec4f8c9dfc95584900':
                #login
                request.session['login'] = request.POST['login_select']
    return redirect('home')

def logout(request):
    if request.session['login']:
        del request.session['login']
    return redirect('home')
