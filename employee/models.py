from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_regNo = models.TextField(unique=True)
    employee_name = models.TextField()
    employee_email = models.TextField()
    employee_mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

#   For Making Data in String Representation in DB
    def __str__(self): 
        return self.employee_name

class Administrator(models.Model):
    adminId = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    status = models.CharField(max_length=50)
    menuId = models.TextField(max_length=20)
    def __str__(self):
        return self.Username

class FoodItem(models.Model):
    foodId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    quantity = models.TextField(max_length=30)
    unitPrice = models.TextField(max_length=30)
    itemCategory = models.CharField(max_length=30)
    def __str__(self):
        return self.Name
    
class Menu(models.Model):
    menuId = models.AutoField(primary_key=True)
    price = models.TextField(max_length=30)
    startDate = models.TextField(max_length=30)
    endDate = models.TextField(max_length=30)
    foodId = models.TextField(max_length=30)
    def __str__(self):
        return self.foodId

class orderItem(models.Model):
    orderId = models.AutoField(primary_key=True)
    foodId = models.TextField(max_length=25)
    quantity = models.TextField(max_length=25)
    unitPrice = models.TextField(max_length=20)
    def __str_(self):
        return self.foodId

class customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    phoneNo = models.TextField(max_length=30)
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    payementId = models.TextField(max_length=50)
    foodId = models.TextField(max_length=40)
    def __str__(self):
        return self.email

class order(models.Model):
    orderId = models.AutoField(primary_key=True)
    orderDate = models.TextField(max_length=30)
    customerId = models.TextField(max_length=30)
    quantity = models.TextField(max_length=30)
    pickUpDate = models.TextField(max_length=30)
    def __str__(self):
        return self.customerId

class payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    customerId = models.TextField(max_length=30)
    orderId = models.TextField(max_length=50)
    paymentDate = models.TextField(max_length=50)
    amount = models.TextField(max_length=30)
    paymentType = models.CharField(max_length=30)
    def __str__(self):
        return self.paymentType

class chef(models.Model):
    chefId = models.AutoField(primary_key=True)
    lName = models.CharField(max_length=30)
    fName = models.CharField(max_length=50)
    UserName = models.CharField(max_length=30)
    phoneNumber = models.TextField(max_length=30)
    password = models.CharField(max_length=40)
    def __str__(self):
        return self.UserName




