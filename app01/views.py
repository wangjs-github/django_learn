from django.shortcuts import render, HttpResponse, reverse


# Create your views here.

def index(request):
    print(reverse("app01:index"))
    return HttpResponse('你好')


def news(request):

    return render(request, "news_index.html", {'name': 'QS'})
