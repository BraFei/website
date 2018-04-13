from django.shortcuts import render, render_to_response
from django.http import HttpResponse


# Create your views here.
def index(req):
    # return HttpResponse('hello')
    return render(req, 'product/index.html')


def chenggonganli(req):
    return render(req, 'product/chenggonganli.html')


def contact(req):
    return render(req, 'product/contact.html')


def product(req):
    return render(req, 'product/product.html')


def new(req):
    return render(req, 'product/new.html')


def aboutme(req):
    return render(req, 'product/aboutme.html')