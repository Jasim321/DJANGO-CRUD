from django.urls import path, include
from .api import EmployeeCreateApi
from .api import EmployeeApi
from .api import EmployeeUpdateApi
from .api import EmployeeDeleteApi
from webbrowser import get
# from employee.views import EmployeeViewSet
from .RenderViews import AdminViewSet, ChefViewSet, CustomerViewSet, FoodItemViewSet, MenuViewSet, OrderItemViewSet, OrderViewSet, PaymentViewSet, listViewSet
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
# router.register(r'users', EmployeeViewSet, basename='user')
# router.register(r'list', EmployeeViewSet, basename='list'),
# router.register(r'create-employee', EmployeeViewSet, basename='create-employee')
router.register(r'list', listViewSet.index, basename='list'),
# router.register(r'create-employee',listViewSet.index, basename='create-employee')
# router.register(r'abc/', EmployeeViewSet)


urlpatterns = [
    # path('api',EmployeeApi.as_view()),
    # path('api/get',EmployeeApi.as_view()),
    # path('api/post',EmployeeViewSet.as_view()),
    # path('hero/get/<int:pk>',views.EmployeeViewSet),
    # path('hero/get/<int:pk>',views.EmployeeViewSet.get),
    # path('api/create',EmployeeCreateApi.as_view()),
    # path('api/<int:pk>',EmployeeUpdateApi.as_view()),
    # path('api/<int:pk>/delete',EmployeeDeleteApi.as_view()),
    # path(r'', include(router.urls)),
    path('', listViewSet.index, name="index-page"),
    # path('list', listViewSet.list,name = "list-page"),
    path('create-employee/', listViewSet.create, name="create-employee"),
    path('create-admin/', AdminViewSet.create, name="create-admin"),
    path('create-fooditem/', FoodItemViewSet.create, name="create-fooditem"),
    path('create-menu/', MenuViewSet.create, name="create-menu"),
    path('create-orderitem/', OrderItemViewSet.create, name="create-orderitem"),
    path('create-customer/', CustomerViewSet.create, name="create-customer"),
    path('create-order/', OrderViewSet.create, name="create-order"),
    path('create-payment/', PaymentViewSet.create, name="create-payment"),
    path('create-chef/', ChefViewSet.create, name="create-chef"),

    path('get-employee/', listViewSet.list, name="get-employee"),
    path('get-admin/', AdminViewSet.list, name="get-admin"),
    path('get-fooditem/', FoodItemViewSet.list, name="get-fooditem"),
    path('get-menu/', MenuViewSet.list, name="get-menu"),
    path('get-orderitem/', OrderItemViewSet.list, name="get-orderitem"),
    path('get-customer/', CustomerViewSet.list, name="get-customer"),
    path('get-order/', OrderViewSet.list, name="get-order"),
    path('get-payment/', PaymentViewSet.list, name="get-payment"),
    path('get-chef/', ChefViewSet.list, name="get-chef"),

    path('update-employee/<int:pk>', listViewSet.update, name="update-employee"),
    path('update-admin/<int:pk>', AdminViewSet.update, name="update-admin"),
    path('update-fooditem/<int:pk>', FoodItemViewSet.update, name="update-fooditem"),
    path('update-menu/<int:pk>', MenuViewSet.update, name="update-menu"),
    path('update-orderitem/<int:pk>', OrderItemViewSet.update, name="update-orderitem"),
    path('update-customer/<int:pk>', CustomerViewSet.update, name="update-customer"),
    path('update-order/<int:pk>', OrderViewSet.update, name="update-order"),
    path('update-payment/<int:pk>', PaymentViewSet.update, name="update-payment"),
    path('update-chef/<int:pk>', ChefViewSet.update, name="update-chef"),

    path('destroy-employee/<int:pk>',listViewSet.destroy, name="destroy-employee"),
    path('destroy-admin/<int:pk>', AdminViewSet.destroy, name="destroy-admin"),
    path('destroy-fooditem/<int:pk>',FoodItemViewSet.destroy, name="destroy-fooditem"),
    path('destroy-menu/<int:pk>', MenuViewSet.destroy, name="destroy-menu"),
    path('destroy-orderitem/<int:pk>',OrderItemViewSet.destroy, name="destroy-orderitem"),
    path('destroy-customer/<int:pk>',CustomerViewSet.destroy, name="destroy-customer"),
    path('destroy-order/<int:pk>', OrderViewSet.destroy, name="destroy-order"),
    path('destroy-payment/<int:pk>', PaymentViewSet.destroy, name="destroy-payment"),
    path('destroy-chef/<int:pk>', ChefViewSet.destroy, name="destroy-chef"),


]
