from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here

def blog_index(request):

    context ={
        'test': 'just for test',
        'welcome': 'hello world!',
    }
    return render(request, 'blog_index.html',context)
