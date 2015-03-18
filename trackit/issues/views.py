from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Label, User, Comment
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

def newusers(request):
    return render(request, 'newusers.html', {"request": request})

def add(request):
    if request.method == 'POST':
        if 'login' in request.session:
            if request.POST['todo'] == "newuser":
                account = request.POST['account']
                name = request.POST['name']
                plain = request.POST['password']
                password = hashlib.sha224(plain.encode()).hexdigest()
                user = User(account=account, name=name, password=password)
                user.save()
                member = request.POST['member']
                if member:
                    user.member = member
                    user.save()
                nickname = request.POST['nickname']
                if nickname != "" and nickname != "User":
                    user.nickname = nickname
                    user.save()

            if request.POST['todo'] == "newissue":
                title = request.POST['title']
                content = request.POST['comment']
                ticket = Ticket(ticket_title=title)
                ticket.save()
                user = get_object_or_404(User, id=1)
                comment = Comment(ticket=ticket, content=content, user=user)
                comment.save()
    return redirect('home')

def edit(request):
    if request.method == 'POST':
        if 'login' in request.session:
            if request.POST['todo'] == "edituser":
                user = get_object_or_404(User, id=request.POST['user_id'])
                user.account = request.POST['account']
                user.name = request.POST['name']
                user.nickname = request.POST['nickname']
                user.member = request.POST['member']
                plain = request.POST['password']
                user.password = hashlib.sha224(plain.encode()).hexdigest()
                user.save()
    return redirect('home')

def users(request, user_id=0):
    if user_id:
        users = get_object_or_404(User, id=user_id)
        u = users
        detail = []
        user_get = {}
        user_get['id'] = u.id
        user_get['account'] = u.account
        user_get['name'] = u.name
        user_get['nickname'] = u.nickname
        user_get['member'] = u.member
        detail.append(user_get)
        return render(request, 'users.html', {"request": request, "detail": detail})
    else:
        users = User.objects.filter().order_by('-id')
        readit = []
        for u in users:
            user_get = {}
            user_get['id'] = u.id
            user_get['account'] = u.account
            user_get['name'] = u.nickname if u.nickname else u.name
            user_get['member'] = u.member
            readit.append(user_get)
            #pass
        return render(request, 'users.html', {"request": request, "readit": readit})

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
