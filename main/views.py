from multiprocessing import context
from django.shortcuts import render
from main.models import *

def Index(request):
    main = Main.objects.all().order_by("-id")[0:4]
    ad = Ad.objects.all().order_by("-id")[0:4]
    recent = Recent.objects.all().order_by("-id")[0:4]
    recentgame = RecentGame.objects.all().order_by("-id")[0:3]
    gameinfo = GameInfo.objects.all().order_by("-id")[0:2]
    context = {
        'main':main,
        'ad':ad,
        'gameinfo':gameinfo,
        'recentgame':recentgame,
        'recent':recent,
    }
    return render(request, "index.html", context)


def Contact(request):
    mapp = Map.objects.last()                                   
    contactus = ContactUs.objects.last()
    context = {
        "contactus": contactus,
        "map": mapp,
    }
    if request.method == "POST":
        d = request.POST
        Email.objects.create(
            name = d.get("name"),
            email = d.get('email'),
            subject = d.get('subject'),
            message = d.get('message')
        )
    return render(request, "contact.html", context)

    # name = models.CharField(max_length=200)
    # email = models.CharField(max_length=200)
    # subject = models.CharField(max_length=200)
    # message = models.CharField(max_length=200)

def Categories(request):
    return render(request, "categories.html")
