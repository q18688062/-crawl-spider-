from django.shortcuts import render
from app01 import models
from utils.paginator import paginator


def index(request):
    return render(request, 'index.html')


def pic(request, name=None):
    t_pic = models.Pic.objects.filter(name=name)[:4]
    if not t_pic:
        t_pic = ['empty.jpg', 'empty.jpg', 'empty.jpg', 'empty.jpg']

    return render(request, 'Simple Image Viewer _ Demo page.html', {'pic': t_pic})



def detail(request):
    all_trunk = models.Trunk.objects.all()
    res = paginator(request.GET.get('page', 1), all_trunk, request.GET.copy(), 15)
    return render(request, 'car_list.html', {'trunks': all_trunk[res.start_data:res.end_data], 'page': res.page_html})



