from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def count(request):
	input = request.GET["fulltext"]
	
	return render(request, 'count.html',{'input':input})
	
def testpage(request):
    return HttpResponse("Test page...This is about me page!!")