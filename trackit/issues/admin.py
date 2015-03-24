from django.contrib import admin
from issues.models import (
    Ticket, Label, User, Comment, TicketStatus, Addlabel,
    )



# Register your models here.
admin.site.register(Ticket)
admin.site.register(Label)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(TicketStatus)
admin.site.register(Addlabel)
