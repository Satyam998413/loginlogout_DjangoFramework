
from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("hello guys blog")
    return render(request,"blog/index.html")

def blogPost(request, slug): 
    return HttpResponse(f'This is blogPost : {slug}')
