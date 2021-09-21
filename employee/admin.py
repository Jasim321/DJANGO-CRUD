from django.contrib import admin
from .models import Administrator, Employee, FoodItem, Menu, chef, customer, order, orderItem, payment
# Register your models here.
admin.site.register(Employee)
admin.site.register(Administrator)
admin.site.register(FoodItem)
admin.site.register(Menu)
admin.site.register(orderItem)
admin.site.register(customer)
admin.site.register(order)
admin.site.register(payment)
admin.site.register(chef)