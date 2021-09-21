from rest_framework import  serializers
from .models import Administrator, Employee, FoodItem, Menu, chef, customer, orderItem, payment

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class orderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderItem
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = chef
        fields = '__all__'