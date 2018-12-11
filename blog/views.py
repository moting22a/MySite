from django.shortcuts import render

# Create your views here.


def index(req):
    return render(req, "base.html")


def work(req):
    return render(req, "work/workbase.html")


def workpycharm(req):
    return render(req, "work/pycharm.html")


def workdjango(req):
    return render(req, "work/django.html")
