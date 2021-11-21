from django.contrib import admin
from .models import Pizza, Salad, Pasta, Side, Dessert, Drink
# Register your models here.


class PizzaAdmin(admin.ModelAdmin):
	list_display = ('name', 'ingredients', 'vegetarian', 'vegan', 'price')
	search_fields = ['name']


admin.site.register(Pizza, PizzaAdmin)


class SaladAdmin(admin.ModelAdmin):
	list_display = ('name', 'ingredients', 'vegetarian', 'vegan', 'price')
	search_fields = ['name']
	
	
admin.site.register(Salad, SaladAdmin)


class PastaAdmin(admin.ModelAdmin):
	list_display = ('name', 'ingredients', 'vegetarian', 'vegan', 'price')
	search_fields = ['name']


admin.site.register(Pasta, PastaAdmin)


class SideAdmin(admin.ModelAdmin):
	list_display = ('name', 'vegetarian', 'vegan', 'price')
	search_fields = ['name']


admin.site.register(Side, SideAdmin)


class DessertAdmin(admin.ModelAdmin):
	list_display = ('name', 'vegetarian', 'vegan', 'price')
	search_fields = ['name']


admin.site.register(Dessert, DessertAdmin)


class DrinkAdmin(admin.ModelAdmin):
	list_display = ('name', 'price')
	search_fields = ['name']


admin.site.register(Drink, DrinkAdmin)
