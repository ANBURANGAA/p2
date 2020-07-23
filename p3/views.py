from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Welcome to the project")
def home(request):
    return render(request,"first.html")
def second(request):
    return render(request,"directory/second.html")
def third(request):
    return render(request,"directory/third.html",context={'data':"Ranga",'name':"Anburangaa"})
def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"directory/fourth.html",{'fruits':fruits})
def fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':50})
def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))
def ab(request,ab):
    a=ab.split(" ")
    sum=int(a[0])+int(a[1])
    return HttpResponse(str(sum))
def greater(request,c,d):
    if(c>d):
        return HttpResponse(c)
    else:
        return HttpResponse(d)
def vowels(request, str):
    vowels = 'aeiouAEIOU'
    vowel = 0
    consonant = 0
    for i in str:
        if i in vowels:
            vowel += 1
        else:
            consonant += 1
    return render(request, 'directry/vowels.html', {'string':str, 'vowel':vowel, 'consonant':consonant})