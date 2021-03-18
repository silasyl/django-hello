from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} of {} years</h1>'.format(nome, idade))

def sum(request, num1, num2):
    return HttpResponse('Sum: {} + {} = {}'.format(num1, num2, num1+num2))

def subtraction(request, num1, num2):
    return HttpResponse('Subtraction: {} - {} = {}'.format(num1, num2, num1-num2))

def product(request, num1, num2):
    return HttpResponse('Product: {} * {} = {}'.format(num1, num2, num1*num2))

def division(request, num1, num2):
    return HttpResponse('Division: {} / {} = {}'.format(num1, num2, num1/num2))