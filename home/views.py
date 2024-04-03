from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):

    table_headings = [
        'S.No','Name','Age','Can Vote',
    ]
    peoples = [
        {'name' : 'nilesh kewale', 'age' : 26},
        {'name' : 'abhishek N', 'age' : 23},
        {'name' : 'Deepanshu churasiya', 'age' : 16},
        {'name' : 'Sandeep', 'age' : 63},
        {'name' : 'Danny Chopra', 'age' : 15},
    ]
    vegetables = ['Pumpkin', 'Tomato', 'Potato']

    context = {
        'page' : 'Home',
        'peoples' : peoples,
        'vegetables' : vegetables,
        'table_headings' :table_headings,
        }

    return render(request , "home/index.html", context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request , "home/contact.html", context)

def about(request):
    context = {'page' : 'About'}
    return render(request , "home/about.html", context)

def success_page(request):
    context = {'page' : 'Success_page'}
    return render(request , "home/success_page.html", context)