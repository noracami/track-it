from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Label, User, Comment
import hashlib

# Create your views here.
def home(request):
    issue = Ticket.objects.filter().order_by('-id')
    readit = []

    if 'label' in request.GET:
        if Label.objects.filter(pk=request.GET['label']).exists():
            label = get_object_or_404(Label, pk=request.GET['label'])
            issue = issue.filter(label=label)

    for i in issue:
        issue_get = {}
        issue_get['id'] = i.id
        issue_get['title'] = i.ticket_title
        issue_get['status'] = i.status
        issue_get['time'] = i.time
        issue_get['label'] = i.label_set.all()
        issue_get['howmanycomments'] = i.Tickets.all().count() - 1
        readit.append(issue_get)
        #pass
    label_list = Label.objects.all().order_by('-id')
    return render(request, 'home.html', {"label_list": label_list, "readit": readit, "request": request})

def issues(request, ticket_id):
    issue = get_object_or_404(Ticket, id=ticket_id)
    issue_get = {}
    issue_get['id'] = issue.id
    issue_get['title'] = issue.ticket_title
    issue_get['status'] = issue.status
    issue_get['time'] = issue.time
    issue_get['label'] = issue.label_set.all()
    issue_get['howmanycomments'] = issue.Tickets.all().count()
    issue_get['comment'] = issue.Tickets.all()
    opened_user = get_object_or_404(User, pk=issue.opened_user.pk)
    opened_user_get = {}
    photo_path = ""
    if 'photo_path' in request.session:
        photo_path = request.session['photo_path']
    else:
        photo_path = "/static/img/user/supportfemale-128.png"

    return render(request, 'issues.html', {
        "photo_path": photo_path,
        "opened_user": opened_user, "issue_get": issue_get, "request": request})

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
        if request.POST['todo'] == "newuser":
            if 'login' in request.session:
                account = request.POST['account']
                name = request.POST['name']
                plain = request.POST['password']
                password = hashlib.sha224(plain.encode()).hexdigest()
                user = User(account=account, name=name, password=password)
                user.save()
                nickname = request.POST['nickname']
                if nickname:
                    user.nickname = nickname
                    user.save()
                member = request.POST['member']
                if member != "" and member != "User":
                    user.member = member
                    user.save()
            return redirect('users')

        if request.POST['todo'] == "newissue":
            if 'login' in request.session:
                title = request.POST['title']
                content = request.POST['comment']
                opened_user = get_object_or_404(User, account=request.session['login'])
                ticket = Ticket(ticket_title=title, opened_user=opened_user)
                ticket.save()
                user = get_object_or_404(User, id=opened_user.id)
                comment = Comment(ticket=ticket, content=content, user=user)
                comment.save()
                return redirect('issues', ticket_id=ticket.id)

        if request.POST['todo'] == "newcomment":
            issue_id = request.POST['issue_id']
            if 'guest' in request.POST:
                user = get_object_or_404(User, id=5)
                ticket = get_object_or_404(Ticket, id=issue_id)
                content = "使用者: %s\n%s" % (request.POST['guestname'] ,request.POST['comment'])
                comment = Comment(user=user, ticket=ticket, content=content)
                comment.save()
            if 'login' in request.session:
                user = get_object_or_404(User, account=request.session['login'])
                ticket = get_object_or_404(Ticket, id=issue_id)
                content = request.POST['comment']
                comment = Comment(user=user, ticket=ticket, content=content)
                comment.save()
            return redirect('issues', ticket_id=issue_id)
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
                if plain:
                    user.password = hashlib.sha224(plain.encode()).hexdigest()
                user.save()
                return redirect('users')
    return redirect('home')

def change_status(request):
    if request.method == 'POST':
        issue_id = request.POST['issue_id']
        if request.POST['todo'] == "addlabels":
            if 'login' in request.session:
                user = get_object_or_404(User, account=request.session['login'])
                ticket = get_object_or_404(Ticket, id=issue_id)
                label = []
                for l in request.POST.getlist('labels'):
                    label += l
                for label_id in label:
                    ticketstatus = TicketStatus(category="addlabels", user=user.id, labels=label_id)
                    ticketstatus.save()
                    ticket.label_set.add(get_object_or_404(Label, id=label_id))
                    ticket.save()
        return redirect('issues', ticket_id=ticket.id)


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
        user_get['photo_path'] = u.photo_path
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
            user_get['photo_path'] = u.photo_path
            readit.append(user_get)
            #pass
        return render(request, 'users.html', {"request": request, "readit": readit})

def loginhere(request):
    if 'errmessage' in request.session:
        errmessage = request.session['errmessage']
        del request.session['errmessage']
        return render(request, 'loginhere.html', {
            "request": request,
            "errmessage": errmessage,
        })
    return render(request, 'loginhere.html', {"request": request})

def login(request):
    #TODO rewrite please
    errmessage = ""
    if request.method == 'POST':
        if 'login_select' in request.POST and 'login_password' in request.POST:
            if User.objects.filter(account=request.POST['login_select']).exists():
                plain = request.POST['login_password']
                password = hashlib.sha224(plain.encode()).hexdigest()
                user = get_object_or_404(User, account=request.POST['login_select'])
                if password == user.password:
                    request.session['login'] = user.account
                    request.session['member'] = user.member
                    request.session['photo_path'] = user.photo_path
                else:
                    errmessage = "wrong password."
                    request.session['errmessage'] = errmessage
                    return redirect('errorinloginhere')
            else:
                errmessage = "account has not exist."
                request.session['errmessage'] = errmessage
                return redirect('errorinloginhere')
        #would'n use
        #if request.POST['login_password']:
        #    plain = request.POST['login_password']
        #    if hashlib.sha224(plain.encode()).hexdigest() == '71454996db126e238e278a202a7dbc49dda187ec4f8c9dfc95584900':
        #        #login
        #        request.session['login'] = request.POST['login_select']
    return redirect('home')

def logout(request):
    if request.session['login']:
        del request.session['login']
        del request.session['member']
    return redirect('home')
