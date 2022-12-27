from django.shortcuts import render, HttpResponse, reverse
import requests


# Create your views here.

def index(request):
    print(reverse("app01:index"))
    return HttpResponse('你好')


def news(req):
    url = 'http://192.168.50.215:8081//admin/device/deviceCount/getNumberEarlier'
    res = requests.get(url)
    res_json = res.json()
    data = res_json['data']
    return render(req, "news/news_index.html", {'name': 'QS', 'data': data})
