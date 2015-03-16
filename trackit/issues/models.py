from django.db import models

# Create your models here.

class Ticket(models.Model):
    class Meta:
        verbose_name = "案件(Ticket)"
    ticket_title = models.CharField("案件主題", max_length=60)
    status = models.BooleanField("結案", default=False)
    time = models.DateTimeField("建立時間", auto_now_add=True)
    def __str__(self):
        return "#%s %s" % (self.id, self.ticket_title)

class Label(models.Model):
    class Meta:
        verbose_name = "標籤(Label)"
    label_name = models.CharField("標籤名稱", max_length=20)
    color = models.CharField("顏色", max_length=6)
    tickets = models.ManyToManyField(Ticket, blank=True)
    def __str__(self):
        return self.label_name
