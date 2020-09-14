from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'Hi': 'Im Haider'})


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    print(worddict)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddict': worddict})


def about(request):
    return render(request, 'about.html')