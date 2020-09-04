from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
 my_title = "hello propertylab..."
 context = {"title": my_title}
 return render(request, "home.html", context)

