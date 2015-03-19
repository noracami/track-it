from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        verbose_name = "使用者(User)"
    account = models.CharField("登入帳號", max_length=30, unique=True)
    name = models.CharField("姓名", max_length=10)
    nickname = models.CharField("暱稱", max_length=40, blank=True)
    member = models.CharField("身分", max_length=20, default="User")
    password = models.CharField("密碼", max_length=56, default="71454996db126e238e278a202a7dbc49dda187ec4f8c9dfc95584900")
    photo_path = models.URLField("大頭照", default="/static/img/user/supportmale-128.png")
    def __str__(self):
        return self.name

class Ticket(models.Model):
    class Meta:
        verbose_name = "案件(Ticket)"
    ticket_title = models.CharField("案件主題", max_length=60)
    status = models.BooleanField("結案", default=False)
    time = models.DateTimeField("建立時間", auto_now_add=True)
    opened_user = models.ForeignKey(User, related_name="OpenedUser")
    def __str__(self):
        return "#%s %s" % (self.id, self.ticket_title)

class Label(models.Model):
    class Meta:
        verbose_name = "標籤(Label)"
    RED = 'e11d21'
    ORANGE = 'eb6420'
    YELLOW = 'fbca04'
    GREEN = '009800'
    DARK_SEA_GREEN = '006b75'
    BLUE = '207de5'
    DARK_BLUE = '0052cc'
    PURPLE = '5319e7'
    LIGHT_RED = 'f7c6c7'
    LIGHT_ORANGE = 'fad8c7'
    LIGHT_YELLOW = 'fef2c0'
    LIGHT_GREEN = 'bfe5bf'
    LIGHT_DARK_SEA_GREEN = 'bfdadc'
    LIGHT_BLUE = 'c7edf8'
    LIGHT_DARK_BLUE = 'bfd4f2'
    LIGHT_PURPLE = 'd4c5f9'
    COLOR_CHOICES = (
        ('MAIN', (
            (RED, '紅色'),
            (ORANGE, '橙色'),
            (YELLOW, '黃色'),
            (GREEN, '綠色'),
            (DARK_SEA_GREEN, '暗綠色'),
            (BLUE, '藍色'),
            (DARK_BLUE, '暗藍色'),
            (PURPLE, '紫色'),
        )),
        ('LIGHT', (
            (LIGHT_RED, '紅色'),
            (LIGHT_ORANGE, '橙色'),
            (LIGHT_YELLOW, '黃色'),
            (LIGHT_GREEN, '綠色'),
            (LIGHT_DARK_SEA_GREEN, '暗綠色'),
            (LIGHT_BLUE, '藍色'),
            (LIGHT_DARK_BLUE, '暗藍色'),
            (LIGHT_PURPLE, '紫色'),
        )),
    )
    color = models.CharField("顏色", max_length=6, choices=COLOR_CHOICES, default=RED)
    WHITE = 'ffffff'
    BLACK = '000000'
    FONTCOLOR_CHOICES = (
        (WHITE, '白'),
        (BLACK, '黑'),
    )
    fontcolor = models.CharField("字的顏色", max_length=6, choices=FONTCOLOR_CHOICES, default=WHITE)
    label_name = models.CharField("標籤名稱", max_length=20)
    tickets = models.ManyToManyField(Ticket, blank=True)
    def __str__(self):
        return self.label_name

class Comment(models.Model):
    class Meta:
        verbose_name = "留言(Comment)"
    user = models.ForeignKey(User, related_name='Users')
    ticket = models.ForeignKey(Ticket, related_name="Tickets")
    content = models.CharField("留言內容", max_length=140, blank=True)
    time = models.DateTimeField("建立時間", auto_now_add=True)

class TicketStatus(models.Model):
    class Meta:
        verbose_name = "狀態(TicketStatus)"
    category = models.CharField("類別", max_length=30)
    user = models.CharField("使用者", max_length=30)
    labels = models.CharField("標籤", max_length=30)
    time = models.DateTimeField("建立時間", auto_now_add=True)
