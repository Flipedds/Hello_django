from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request,nome,idade):
	return HttpResponse('<h1>hello {} de {} anos </h1>'.format(nome,idade))

def soma(request,valor1,valor2):
	soma = valor1 + valor2
	return HttpResponse('<h1>Soma = {}</h1>'.format(soma))
def subtra(request,valor1,valor2):
	subtra = valor1 - valor2
	return HttpResponse('<h1>Subtra = {}</h1>'.format(subtra))

def div(request,valor1,valor2):
	div = valor1 / valor2
	return HttpResponse('<h1>mult = {}</h1>'.format(div))

def mult(request,valor1,valor2):
	mult = valor1 * valor2
	return HttpResponse('<h1>div = {}</h1>'.format(mult))

