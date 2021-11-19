from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.


# always put request because this is going to be an HTTP Request
# /menu
def index(request):
	"""
	pizzas = Pizza.objects.all()
	print(pizzas)
	pizzas_names_prices = [pizza.name + " : $" + str(pizza.price) for pizza in pizzas]
	# for pizza in pizzas:
	# 	pizzas_names = pizza.name
	pizzas_names_prices_str = ", ".join(pizzas_names_prices)
	"""
	pizzas = Pizza.objects.all().order_by('price')
	return render(request, 'menu/index.html', {'pizzas': pizzas})

