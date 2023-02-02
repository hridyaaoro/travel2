from django.shortcuts import render
from django.http import HttpResponse

from . models import Place,ot_places


def demo(request):
    obj=Place.objects.all()
    plc = ot_places.objects.all()
    return render(request,'index.html',{'result':obj,'other_places':plc})