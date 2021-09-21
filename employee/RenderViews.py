from django.shortcuts import render, redirect
from .models import Employee,customer,orderItem,chef,payment,order,Menu,FoodItem,Administrator
from .serializer import EmployeeSerializer,AdministratorSerializer,ChefSerializer,CustomerSerializer,MenuSerializer,orderItemSerializer,FoodItemSerializer,orderSerializer,PaymentSerializer

# from rest_framework.decorators import action, api_view
from django.http import JsonResponse
# from .views import HttpResponse
# from rest_framework.parsers import JSONParser 
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
import json

class listViewSet(viewsets.ModelViewSet):
	def index(request):
		name = Employee.objects.values('employee_name')
		print(request.__dict__)
		return render(request,'employee/index.html')
	

	def retrieve(self, request, pk=0):
		print("-----------------------------")
		print("Inside Render Get()")
		print("-----------------------------")
		try:
			Emp = get_object_or_404(Employee, pk=pk)
			return JsonResponse({
				"employee_regNo": Emp.employee_regNo,
				"emplyee_name": Emp.employee_name,
				"employee_email": Emp.employee_email,
				"employee_mobile": Emp.employee_mobile
			})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Record Doesn't exists"
			})

	#Retrieving all Objects
	def list(request):
		# print("--------------------------")
		# print("Inside Render List()")
		# print("--------------------------")
		try:
			Emp = Employee.objects.all()
			data_list = []
			for i in Emp:
				# print(i.__dict__)
				data_list.append({
				"employee_id": i.employee_id,
				"employee_regNo": i.employee_regNo,
				"emplyee_name": i.employee_name,
				"employee_email":i.employee_email,
				"employee_mobile": i.employee_mobile
				})
			# print(data_list)
			return render(request ,'employee/get.html' , {'data': data_list})
			# return JsonResponse({
			# 	"Status": data_list
			# 	})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Fail to Retrieve Entire DB!"
				})

	#POST request for creating a new record
	def create(request):
		# print("------------------",request._post['employee_regNo'])
		
		# print("------------------")
		try:
			# print(request)
			# print(request._post)
			# print(request.__dict__)
			print("Start of Try Block")				
			# print("request",request.__dict__)
			print("Middle of Try Block")
			print("----------------------")
			print(request.method)
			print("----------------------")
			obj = Employee()
			if(request.method == 'POST'):	
				print("Inside Post Request()")
				obj.employee_regNo = request._post['employee_regNo']
				obj.employee_name = request._post['username']
				obj.employee_email = request._post['email']
				obj.employee_mobile = request._post['number']
				obj.save()
				return redirect('create-employee')
			else:
				return render(request,'employee/create.html')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "OOPS! Records Already Exists!"
			})


	def update(request, pk=None): #Update request for updating a record or Modifying Record
		print("---------------------")
		print("Inside Update()")
		print(request.method)
		print("---------------------")
		try:
			print("Start of Update")
			print("--------------------------------")
			print(pk)
			obj = Employee.objects.get(employee_id=pk)
			print("--------------------------------")
			print(request.method)
			if(request.method == 'POST'):	
				print("Inside Post Request()")
				obj.employee_regNo = request._post['employee_regNo']
				obj.employee_name = request._post['username']
				obj.employee_email = request._post['email']
				obj.employee_mobile = request._post['number']
				obj.save()
				return redirect('get-employee')
			else:
				return render(request,'employee/update.html', {'data': obj, 'pk':pk})

		# 	return JsonResponse({
		# 	"Status": "Successfully Updated"
		# })
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Updating Data"
		})

	#Delete request for deleting a certain record by the PK
	def destroy(request, pk=None):
		print("--------------------")
		print("Inside Destroy()")
		print("--------------------")
		print(pk)
		try:
			# Emp = Employee.objects.all()
			obj = Employee.objects.get(employee_id=pk)
			obj.delete()
			return redirect('get-employee')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Deleting data from db",
			})

class AdminViewSet(viewsets.ModelViewSet):
	
	# def index(request):
	# 	name = Administrator.objects.values('Username')
	# 	print(name)
	# 	return render(request,'employee/index.html')
	
	def retrieve(self, request, pk=0):
		print("-----------------------------")
		print("Inside Retrieve()")
		print("-----------------------------")
		try:
			Admin = get_object_or_404(Administrator, pk=pk)
			return JsonResponse({
				"fName": Admin.fName,
				"lName": Admin.lName,
				"Username": Admin.Username,
				"Password": Admin.Password,
				"status": Admin.status,
				"menuId": Admin.menuId,
			})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Record Doesn't exists"
			})

	#Retrieving all Objects
	def list(request):
		print("--------------------------")
		print("Inside list()")
		print("--------------------------")

		try:
			Admin = Administrator.objects.all()
			print(Admin.__dict__)
			data_list = []
			for i in Admin:
				print(i.__dict__)
				data_list.append({
				"adminId": i.adminId,
				"fName": i.fName,
				"lName": i.lName,
				"Username": i.Username,
				"Password": i.Password,
				"status": i.status,
				"menuId": i.menuId,
				})
			# print(data_list)
			print("-Inside k()")
			for j in data_list:
				print(j)
			print(data_list)
			return render(request, 'employee/Admin/get.html', {'data': data_list})
			# return JsonResponse({
			# 	"Status": data_list
			# 	})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Fail to Retrieve Entire DB!"
				})

	#POST request for creating a new record
	def create(request):
		# print("------------------",request._post['employee_regNo'])
		print("------------------")
		print("Inside create()")
		print("------------------")
		try:
			# print(request)
			# print(request._post)
			# print(request.__dict__)
			print("Start of Try Block")				
			# print("request",request.__dict__)
			print("Middle of Try Block")
			print("-------------------------------")
			print(request.method)
			print("-------------------------------")

			obj = Administrator()
			
			if(request.method == 'POST'):
				print(request.method)	
				print("Inside Post Request()")
				obj.fName = request._post['fName']
				# print(obj.fName)
				obj.lName = request._post['lName']
				obj.Username = request._post['Username']
				obj.Password = request._post['Password']
				obj.status = request._post['status']
				obj.menuId = request._post['menuId']
				obj.save()
				return redirect('get-admin')
			else:
				return render(request,'employee/Admin/create.html')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "OOPS! Records Already Exists!"
			})


	def update(request, pk=None): #Update request for updating a record or Modifying Record
		print("---------------------")
		print("Inside Update()")
		print(request.method)
		print("---------------------")
		try:
			print("Start of Update")
			print("--------------------------------")
			print(pk)
			print("------------------------------")
			obj = Administrator.objects.get(adminId=pk)
			print(obj.adminId)
			print("--------------------------------")
			print(request.method)
			if(request.method == 'POST'):	
				print("Inside Post Request()")
				obj.fName = request._post['fName']
				obj.lName = request._post['lName']
				obj.Username = request._post['Username']
				obj.Password = request._post['Password']
				obj.save()
				return redirect('get-admin')
			else:
				return render(request,'employee/Admin/update.html', {'data': obj, 'pk':pk})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Updating Data"
		})

	# #Delete request for deleting a certain record by the PK
	def destroy(request, pk=None):
		print("--------------------")
		print("Inside Destroy()")
		print("--------------------")
		print(pk)
		try:
			# Emp = Employee.objects.all()
			obj = Administrator.objects.get(adminId=pk)
			obj.delete()
			return redirect('get-admin')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Deleting data from db",
			})


class FoodItemViewSet(viewsets.ModelViewSet):
	
	# def index(request):
	# 	name = Administrator.objects.values('Username')
	# 	print(name)
	# 	return render(request,'employee/index.html')
	
	# def retrieve(self, request, pk=0):
	# 	print("-----------------------------")
	# 	print("Inside Retrieve()")
	# 	print("-----------------------------")
	# 	try:
	# 		Admin = get_object_or_404(Administrator, pk=pk)
	# 		return JsonResponse({
	# 			"fName": Admin.fName,
	# 			"lName": Admin.lName,
	# 			"Username": Admin.Username,
	# 			"Password": Admin.Password,
	# 			"status": Admin.status,
	# 			"menuId": Admin.menuId,
	# 		})
	# 	except Exception as e:
	# 		print(e)
	# 		return JsonResponse({
	# 			"Status": "Record Doesn't exists"
	# 		})

	#Retrieving all Objects
	def list(request):
		print("--------------------------")
		print("Inside list()")
		print("--------------------------")

		try:
			food = FoodItem.objects.all()
			print(food.__dict__)
			data_list = []
			for i in food:
				print(i.__dict__)
				data_list.append({
				"foodId": i.foodId,
				"name": i.Name,
				"quantity": i.quantity,
				"unitPrice": i.unitPrice,
				"itemCategory": i.itemCategory
				})

			# print(data_list)
			print("-Inside k()")
			for j in data_list:
				print(j)
			print(data_list)
			return render(request, 'employee/FoodItem/get.html', {'data': data_list})
			# return JsonResponse({
			# 	"Status": data_list
			# 	})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Fail to Retrieve Entire DB!"
				})

	#POST request for creating a new record
	def create(request):
		# print("------------------",request._post['employee_regNo'])
		print("------------------")
		print("Inside create()")
		print("------------------")
		try:
			# print(request)
			# print(request._post)
			# print(request.__dict__)
			print("Start of Try Block")				
			# print("request",request.__dict__)
			print("Middle of Try Block")
			print("-------------------------------")
			print(request.method)
			print("-------------------------------")

			obj = FoodItem()
			
			if(request.method == 'POST'):
				print(request.method)	
				print("Inside Post Request()")
				obj.Name = request._post['Name']
				obj.quantity = request._post['quantity']
				obj.unitPrice = request._post['unitPrice']
				obj.itemCategory = request._post['itemCategory']
				obj.save()
				return redirect('get-fooditem')
			else:
				return render(request,'employee/FoodItem/create.html')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "OOPS! Records Already Exists!"
			})


	def update(request, pk=None): #Update request for updating a record or Modifying Record
		print("---------------------")
		print("Inside Update()")
		print(request.method)
		print("---------------------")
		try:
			print("Start of Update")
			print("--------------------------------")
			print(pk)
			print("------------------------------")
			obj = FoodItem.objects.get(foodId=pk)
			print(obj.foodId)
			print("--------------------------------")
			print(request.method)
			if(request.method == 'POST'):	
				print("Inside Post Request()")
				obj.Name = request._post['Name']
				obj.quantity = request._post['quantity']
				obj.unitPrice = request._post['unitPrice']
				obj.itemCategory = request._post['itemCategory']
				obj.save()
				return redirect('get-fooditem')
			else:
				return render(request,'employee/FoodItem/update.html', {'data': obj, 'pk':pk})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Updating Data"
		})

	# # #Delete request for deleting a certain record by the PK
	def destroy(request, pk=None):
		print("--------------------")
		print("Inside Destroy()")
		print("--------------------")
		print(pk)
		try:
			# Emp = Employee.objects.all()
			obj = FoodItem.objects.get(foodId=pk)
			obj.delete()
			return redirect('get-fooditem')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Deleting data from db",
			})


class MenuViewSet(viewsets.ModelViewSet):
	
	# def retrieve(self, request, pk=0):
	# 	print("-----------------------------")
	# 	print("Inside Retrieve()")
	# 	print("-----------------------------")
	# 	try:
	# 		Admin = get_object_or_404(Administrator, pk=pk)
	# 		return JsonResponse({
	# 			"menuId": i.menuId,
	# 			"price": i.price,
	# 			"startDate": i.startDate,
	# 			"endDate": i.endDate,
	# 			"foodId": i.foodId
	# 		})
	# 	except Exception as e:
	# 		print(e)
	# 		return JsonResponse({
	# 			"Status": "Record Doesn't exists"
	# 		})

	#Retrieving all Objects
	def list(request):
		print("--------------------------")
		print("Inside list()")
		print("--------------------------")

		try:
			men = Menu.objects.all()
			print(men.__dict__)
			data_list = []
			for i in men:
				print(i.__dict__)
				data_list.append({
				"menuId": i.menuId,
				"price": i.price,
				"startDate": i.startDate,
				"endDate": i.endDate,
				"foodId": i.foodId
				})

			# print(data_list)
			print("-Inside k()")
			for j in data_list:
				print(j)
			print(data_list)
			return render(request, 'employee/Menu/get.html', {'data': data_list})
			# return JsonResponse({
			# 	"Status": data_list
			# 	})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Fail to Retrieve Entire DB!"
				})

	#POST request for creating a new record
	def create(request):
		# print("------------------",request._post['employee_regNo'])
		print("------------------")
		print("Inside create()")
		print("------------------")
		try:
			# print(request)
			# print(request._post)
			# print(request.__dict__)
			print("Start of Try Block")				
			# print("request",request.__dict__)
			print("Middle of Try Block")
			print("-------------------------------")
			print(request.method)
			print("-------------------------------")

			obj = Menu()
			
			if(request.method == 'POST'):
				print(request.method)	
				print("Inside Post Request()")
				obj.price = request._post['price']
				obj.startDate = request._post['startDate']
				obj.endDate = request._post['endDate']
				obj.foodId = request._post['foodId']
				obj.save()
				return redirect('get-menu')
			else:
				return render(request,'employee/Menu/create.html')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "OOPS! Records Already Exists!"
			})


	def update(request, pk=None): #Update request for updating a record or Modifying Record
		print("---------------------")
		print("Inside Update()")
		print(request.method)
		print("---------------------")
		try:
			print("Start of Update")
			print("--------------------------------")
			print(pk)
			print("------------------------------")
			obj = Menu.objects.get(menuId=pk)
			print(obj.menuId)
			print("--------------------------------")
			print(request.method)
			if(request.method == 'POST'):	
				print("Inside Post Request()")
				obj.price = request._post['price']
				obj.startDate = request._post['startDate']
				obj.endDate = request._post['endDate']
				obj.foodId = request._post['foodId']
				obj.save()
				return redirect('get-menu')
			else:
				return render(request,'employee/Menu/update.html', {'data': obj, 'pk':pk})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Updating Data"
		})

	# # #Delete request for deleting a certain record by the PK
	def destroy(request, pk=None):
		print("--------------------")
		print("Inside Destroy()")
		print("--------------------")
		print(pk)
		try:
			# Emp = Employee.objects.all()
			obj = Menu.objects.get(menuId=pk)
			obj.delete()
			return redirect('get-menu')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Deleting data from db",
			})

class OrderItemViewSet(viewsets.ModelViewSet):
	
	# def retrieve(self, request, pk=0):
	# 	print("-----------------------------")
	# 	print("Inside Retrieve()")
	# 	print("-----------------------------")
	# 	try:
	# 		Admin = get_object_or_404(Administrator, pk=pk)
	# 		return JsonResponse({
	# 			"menuId": i.menuId,
	# 			"price": i.price,
	# 			"startDate": i.startDate,
	# 			"endDate": i.endDate,
	# 			"foodId": i.foodId
	# 		})
	# 	except Exception as e:
	# 		print(e)
	# 		return JsonResponse({
	# 			"Status": "Record Doesn't exists"
	# 		})

	#Retrieving all Objects
	def list(request):
		print("--------------------------")
		print("Inside Order-Item list()")
		print("--------------------------")

		try:
			oI = orderItem.objects.all()
			print(oI.__dict__)
			data_list = []
			for i in oI:
				print(i.__dict__)
				data_list.append({
				"orderId": i.orderId,
				"foodId": i.foodId,
				"quantity": i.quantity,
				"unitPrice": i.unitPrice
				})

			# print(data_list)
			print("-Inside k()")
			for j in data_list:
				print(j)
			print(data_list)
			return render(request, 'employee/OrderItem/get.html', {'data': data_list})
			# return JsonResponse({
			# 	"Status": data_list
			# 	})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Fail to Retrieve Entire DB!"
				})

	# #POST request for creating a new record
	def create(request):
		# print("------------------",request._post['employee_regNo'])
		print("------------------")
		print("Inside create()")
		print("------------------")
		try:
			# print(request)
			# print(request._post)
			# print(request.__dict__)
			print("Start of Try Block")				
			# print("request",request.__dict__)
			print("Middle of Try Block")
			print("-------------------------------")
			print(request.method)
			print("-------------------------------")

			obj = orderItem()
			
			if(request.method == 'POST'):
				print(request.method)	
				print("Inside Post Request()")
				obj.foodId = request._post['foodId']
				obj.quantity = request._post['quantity']
				obj.unitPrice = request._post['unitPrice']
				obj.save()
				return redirect('get-orderitem')
			else:
				return render(request,'employee/OrderItem/create.html')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "OOPS! Records Already Exists!"
			})


	def update(request, pk=None): #Update request for updating a record or Modifying Record
		print("---------------------")
		print("Inside Update()")
		print(request.method)
		print("---------------------")
		try:
			print("Start of Update")
			print("--------------------------------")
			print(pk)
			print("------------------------------")
			obj = orderItem.objects.get(orderId=pk)
			print(obj.orderId)
			print("--------------------------------")
			print(request.method)
			if(request.method == 'POST'):	
				print("Inside Post Request()")
				obj.foodId = request._post['foodId']
				obj.quantity = request._post['quantity']
				obj.unitPrice = request._post['unitPrice']
				obj.save()
				return redirect('get-orderitem')
			else:
				return render(request,'employee/OrderItem/update.html', {'data': obj, 'pk':pk})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Updating Data"
		})

	# # #Delete request for deleting a certain record by the PK
	def destroy(request, pk=None):
		print("--------------------")
		print("Inside Destroy()")
		print("--------------------")
		print(pk)
		try:
			# Emp = Employee.objects.all()
			obj = orderItem.objects.get(orderId=pk)
			obj.delete()
			return redirect('get-orderitem')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Deleting data from db",
			})



class CustomerViewSet(viewsets.ModelViewSet):

	#Retrieving all Objects
	def list(request):
		print("--------------------------")
		print("Inside Customer list()")
		print("--------------------------")

		try:
			oI = customer.objects.all()
			print(oI.__dict__)
			data_list = []
			for i in oI:
				print(i.__dict__)
				data_list.append({
				"customerId": i.customerId,
				"email": i.email,
				"fName": i.fName,
				"lName": i.lName,
				"payementId": i.payementId,
				"foodId": i.foodId,
				})

			# print(data_list)
			print("-Inside k()")
			for j in data_list:
				print(j)
			print(data_list)
			return render(request, 'employee/Customer/get.html', {'data': data_list})
			# return JsonResponse({
			# 	"Status": data_list
			# 	})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Fail to Retrieve Entire DB!"
				})

	# #POST request for creating a new record
	def create(request):
		# print("------------------",request._post['employee_regNo'])
		print("------------------")
		print("Inside create()")
		print("------------------")
		try:
			# print(request)
			# print(request._post)
			# print(request.__dict__)
			print("Start of Try Block")				
			# print("request",request.__dict__)
			print("Middle of Try Block")
			print("-------------------------------")
			print(request.method)
			print("-------------------------------")

			obj = customer()
			
			if(request.method == 'POST'):
				print(request.method)	
				print("Inside Post Request()")
				obj.email = request._post['email']
				obj.phoneNo = request._post['phoneNo']
				obj.fName = request._post['fName']
				obj.lName = request._post['lName']
				obj.payementId = request._post['payementId']
				obj.foodId = request._post['foodId']
				obj.save()
				return redirect('get-customer')
			else:
				return render(request,'employee/Customer/create.html')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "OOPS! Records Already Exists!"
			})


	def update(request, pk=None): #Update request for updating a record or Modifying Record
		print("---------------------")
		print("Inside Customer Update()")
		print(request.method)
		print("---------------------")
		try:
			print("Start of Update")
			print("--------------------------------")
			print(pk)
			print("------------------------------")
			obj = customer.objects.get(customerId=pk)
			# print(obj.orderId)
			print("--------------------------------")
			print(request.method)
			if(request.method == 'POST'):	
				print("Inside Post Request()")
				obj.email = request._post['email']
				obj.phoneNo = request._post['phoneNo']
				obj.fName = request._post['fName']
				obj.lName = request._post['lName']
				obj.payementId = request._post['payementId']
				obj.foodId = request._post['foodId']
				obj.save()
				return redirect('get-customer')
			else:
				return render(request,'employee/Customer/update.html', {'data': obj, 'pk':pk})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Updating Data"
		})

	# # #Delete request for deleting a certain record by the PK
	def destroy(request, pk=None):
		print("--------------------")
		print("Inside Destroy()")
		print("--------------------")
		print(pk)
		try:
			# Emp = Employee.objects.all()
			obj = customer.objects.get(customerId=pk)
			obj.delete()
			return redirect('get-customer')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Deleting data from db",
			})

class OrderViewSet(viewsets.ModelViewSet):

	#Retrieving all Objects
	def list(request):
		print("--------------------------")
		print("Inside Customer list()")
		print("--------------------------")

		try:
			oI = order.objects.all()
			print(oI.__dict__)
			data_list = []
			for i in oI:
				print(i.__dict__)
				data_list.append({
				"orderId": i.orderId,
				"orderDate": i.orderDate,
				"customerId": i.customerId,
				"quantity": i.quantity,
				"pickUpDate": i.pickUpDate,
				})

			# print(data_list)
			print("-Inside k()")
			for j in data_list:
				print(j)
			print(data_list)
			return render(request, 'employee/Order/get.html', {'data': data_list})
			# return JsonResponse({
			# 	"Status": data_list
			# 	})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Fail to Retrieve Entire DB!"
				})

	# #POST request for creating a new record
	def create(request):
		# print("------------------",request._post['employee_regNo'])
		print("------------------")
		print("Inside create()")
		print("------------------")
		try:
			# print(request)
			# print(request._post)
			# print(request.__dict__)
			print("Start of Try Block")				
			# print("request",request.__dict__)
			print("Middle of Try Block")
			print("-------------------------------")
			print(request.method)
			print("-------------------------------")

			obj = order()
			
			if(request.method == 'POST'):
				print(request.method)	
				print("Inside Post Request()")
				obj.orderDate = request._post['orderDate']
				obj.customerId = request._post['customerId']
				obj.quantity = request._post['quantity']
				obj.pickUpDate = request._post['pickUpDate']
				obj.save()
				return redirect('get-order')
			else:
				return render(request,'employee/Order/create.html')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "OOPS! Records Already Exists!"
			})


	def update(request, pk=None): #Update request for updating a record or Modifying Record
		print("---------------------")
		print("Inside Customer Update()")
		print(request.method)
		print("---------------------")
		try:
			print("Start of Update")
			print("--------------------------------")
			print(pk)
			print("------------------------------")
			obj = order.objects.get(orderId=pk)
			# print(obj.orderId)
			print("--------------------------------")
			print(request.method)
			if(request.method == 'POST'):	
				print("Inside Post Request()")
				obj.orderId = request._post['orderId']
				obj.orderDate = request._post['orderDate']
				obj.customerId = request._post['customerId']
				obj.quantity = request._post['quantity']
				obj.pickUpDate = request._post['pickUpDate']
				obj.save()
				return redirect('get-order')
			else:
				return render(request,'employee/Order/update.html', {'data': obj, 'pk':pk})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Updating Data"
		})

	# # #Delete request for deleting a certain record by the PK
	def destroy(request, pk=None):
		print("--------------------")
		print("Inside Destroy()")
		print("--------------------")
		print(pk)
		try:
			# Emp = Employee.objects.all()
			obj = order.objects.get(orderId=pk)
			obj.delete()
			return redirect('get-order')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Deleting data from db",
			})

class PaymentViewSet(viewsets.ModelViewSet):

	#Retrieving all Objects
	def list(request):
		print("--------------------------")
		print("Inside Customer list()")
		print("--------------------------")

		try:
			oI = payment.objects.all()
			print(oI.__dict__)
			data_list = []
			for i in oI:
				print(i.__dict__)
				data_list.append({
				"paymentId": i.paymentId,
				"customerId": i.customerId,
				"orderId": i.orderId,
				"paymentDate": i.paymentDate,
				"amount": i.amount,
				"paymentType": i.paymentType,
				})

			# print(data_list)
			print("-Inside k()")
			for j in data_list:
				print(j)
			print(data_list)
			return render(request, 'employee/Payment/get.html', {'data': data_list})
			# return JsonResponse({
			# 	"Status": data_list
			# 	})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Fail to Retrieve Entire DB!"
				})

	# #POST request for creating a new record
	def create(request):
		# print("------------------",request._post['employee_regNo'])
		print("------------------")
		print("Inside create()")
		print("------------------")
		try:
			# print(request)
			# print(request._post)
			# print(request.__dict__)
			print("Start of Try Block")				
			# print("request",request.__dict__)
			print("Middle of Try Block")
			print("-------------------------------")
			print(request.method)
			print("-------------------------------")

			obj = payment()
			
			if(request.method == 'POST'):
				print(request.method)	
				print("Inside Post Request()")
				obj.customerId = request._post['customerId']
				obj.orderId = request._post['orderId']
				obj.paymentDate = request._post['paymentDate']
				obj.amount = request._post['amount']
				obj.paymentType = request._post['paymentType']
				obj.save()
				return redirect('get-payment')
			else:
				return render(request,'employee/Payment/create.html')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "OOPS! Records Already Exists!"
			})


	def update(request, pk=None): #Update request for updating a record or Modifying Record
		print("---------------------")
		print("Inside Customer Update()")
		print(request.method)
		print("---------------------")
		try:
			print("Start of Update")
			print("--------------------------------")
			print(pk)
			print("------------------------------")
			obj = payment.objects.get(paymentId=pk)
			print("--------------------------------")
			print(request.method)
			if(request.method == 'POST'):	
				print("Inside Post Request()")
				obj.paymentId = request._post['paymentId']
				obj.customerId = request._post['customerId']
				obj.orderId = request._post['orderId']
				obj.paymentDate = request._post['paymentDate']
				obj.amount = request._post['amount']
				obj.paymentType = request._post['paymentType']
				obj.save()
				return redirect('get-payment')
			else:
				return render(request,'employee/Payment/update.html', {'data': obj, 'pk':pk})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Updating Data"
		})

	# # #Delete request for deleting a certain record by the PK
	def destroy(request, pk=None):
		print("--------------------")
		print("Inside Destroy()")
		print("--------------------")
		print(pk)
		try:
			# Emp = Employee.objects.all()
			obj = payment.objects.get(paymentId=pk)
			obj.delete()
			return redirect('get-payment')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Deleting data from db",
			})

class ChefViewSet(viewsets.ModelViewSet):

	#Retrieving all Objects
	def list(request):
		print("--------------------------")
		print("Inside Customer list()")
		print("--------------------------")

		try:
			oI = chef.objects.all()
			print(oI.__dict__)
			data_list = []
			for i in oI:
				print(i.__dict__)
				data_list.append({
				"chefId": i.chefId,
				"lName": i.lName,
				"fName": i.fName,
				"UserName": i.UserName,
				"phoneNumber": i.phoneNumber,
				"password": i.password
				})
			# print(data_list)
			print("-Inside k()")
			for j in data_list:
				print(j)
			print(data_list)
			return render(request, 'employee/Chef/get.html', {'data': data_list})
			# return JsonResponse({
			# 	"Status": data_list
			# 	})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Fail to Retrieve Entire DB!"
				})

	# #POST request for creating a new record
	def create(request):
		# print("------------------",request._post['employee_regNo'])
		print("------------------")
		print("Inside create()")
		print("------------------")
		try:
			# print(request)
			# print(request._post)
			# print(request.__dict__)
			print("Start of Try Block")				
			# print("request",request.__dict__)
			print("Middle of Try Block")
			print("-------------------------------")
			print(request.method)
			print("-------------------------------")

			obj = chef()
			
			if(request.method == 'POST'):
				print(request.method)	
				print("Inside Post Request()")
				# obj.chefId = request._post['chefId']
				obj.lName = request._post['lName']
				obj.fName = request._post['fName']
				obj.UserName = request._post['UserName']
				obj.phoneNumber = request._post['phoneNumber']
				obj.password = request._post['password']
				obj.save()
				return redirect('get-chef')
			else:
				return render(request,'employee/Chef/create.html')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "OOPS! Records Already Exists!"
			})


	def update(request, pk=None): #Update request for updating a record or Modifying Record
		print("---------------------")
		print("Inside Customer Update()")
		print(request.method)
		print("---------------------")
		try:
			print("Start of Update")
			print("--------------------------------")
			print(pk)
			print("------------------------------")
			obj = chef.objects.get(chefId=pk)
			print("--------------------------------")
			print(request.method)
			if(request.method == 'POST'):	
				print("Inside Post Request()")
				#Not Pass ID here.Because Id is already selected in above lines
				obj.lName = request._post['lName']
				obj.fName = request._post['fName']
				obj.UserName = request._post['UserName']
				obj.phoneNumber = request._post['phoneNumber']
				obj.password = request._post['password']
				obj.save()
				return redirect('get-chef')
			else:
				return render(request,'employee/Chef/update.html', {'data': obj, 'pk':pk})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Updating Data"
		})

	# # #Delete request for deleting a certain record by the PK
	def destroy(request, pk=None):
		print("--------------------")
		print("Inside Destroy()")
		print("--------------------")
		print(pk)
		try:
			# Emp = Employee.objects.all()
			obj = chef.objects.get(chefId=pk)
			obj.delete()
			return redirect('get-chef')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Deleting data from db",
			})