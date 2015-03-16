from django.shortcuts import render
from .models import Ticket, Label

# Create your views here.
def home(request):
    issue = Ticket.objects.filter().order_by('-id')
    label = Label.objects.filter().order_by('-id')
    readit = []
    for ticket in issue:
        readit.append(ticket.label_set.all())
        pass#a
    return render(request, 'home.html', {"issue": issue, "label": label, "readit": readit})
