from django.urls import path
from . import views

urlpatterns = [   
    path('',views.GetAllEmployees,name='index'),
    path('GetEmployeeById/<int:pk>',views.one_data),
    path('CreateEmp/',views.create_data),
    path('UpdateEmp/<int:pk>',views.update_data),
    path('DeleteEmp/<int:pk>',views.delete_data),
]
