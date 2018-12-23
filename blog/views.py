from django.shortcuts import render
from blog import models
# Create your views here.


def index(req):
    return render(req, "base.html")


def abc(req):
    return render(req, "abc.html")


def typeIndex(req, typeid):
    contents = models.Content.objects.filter(content_type=typeid).order_by("-create_time")
    return render(req, "typeIndex.html", locals())


def detail(req, contentid):
    curcont = models.Content.objects.filter(id=contentid).first()
    contentType = curcont.content_type
    contents = models.Content.objects.filter(content_type=contentType).order_by("-create_time")

    return render(req, "detail.html", locals())
