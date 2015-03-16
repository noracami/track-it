from django.contrib import admin
from issues.models import (
    Ticket, Label,
    )



# Register your models here.
admin.site.register(Ticket)
admin.site.register(Label)
