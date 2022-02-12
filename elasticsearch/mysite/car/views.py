from django.shortcuts import render
from .documents import CarDocument

# Create your views here.

def search(request):
    s = CarDocument.search().query()
    qs = s.to_queryset()
    for car in qs:
        print("*"*80, car.color)


def ali(request):
    s = CarDocument.search().query("match", name="pride")
    qs = s.to_queryset()
    car = qs[0]
    car.name = 'samand'
    car.save()
    print("*"*80, car)


def ali2(request):
    s = CarDocument.search().query("match", name="samand")
    qs = s.to_queryset()
    car = qs[0]
    print("*"*80,"\n",{"name":car.name}, {"age":car.age}, {"color":car.color})